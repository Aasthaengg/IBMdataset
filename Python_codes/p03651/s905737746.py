#!/usr/bin/env python3
def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b % a, a)


n, k = map(int, input().split())
a = list(map(int, input().split()))
max_a = max(a)
a_gcd = a[0]
for x in a:
    a_gcd = gcd(a_gcd, x)
if k <= max_a and k % a_gcd == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


"""
どれだけ小さい差を作れるかがポイント
maxの値からそれを引くことでいろんな値を作ることができる
もし差が1を作れればmax 以下の値全て作れる
N この最大公約数が最小の差になる
"""
