# https://atcoder.jp/contests/agc038/tasks/agc038_a

from itertools import combinations

H, W, A, B = map(int, input().split())

for _ in range(B):
    print("0" * A + "1" * (W-A))
for _ in range(H - B):
    print("1" * A + "0" * (W-A))