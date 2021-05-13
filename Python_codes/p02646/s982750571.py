# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b

"""
   A(V)             B(W)
---------------------------------

"""

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V < W:
    print("NO")
else:
    if abs(B - A) <= abs(W - V) * T:
        print("YES")
    else:
        print("NO")