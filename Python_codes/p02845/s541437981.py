#三井住友信託銀行プログラミングコンテスト2019 -E Colorful Hats 2
"""
適当に色を割り振って良い。
[0,0,0]の状態から、その数字がいくつあるかを掛けていく
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = list(map(int,readline().split()))
mod = 10**9+7

RGB = [0,0,0]
ans = 1
for i in lst1:
    ans*= RGB.count(i)
    ans %= mod
    if not ans:
        print(ans)
        exit()
    for j in range(3):
        if RGB[j] == i:
            RGB[j] += 1
            break
print(ans)