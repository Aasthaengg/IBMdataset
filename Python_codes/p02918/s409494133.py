"""
1度の操作で最大+2できる
隣り合う箇所はN-1
LないしRが連続している箇所をグループとして見ると、求める数は
  N-1-隣り合うグループが異なっている場所の個数
= N-1-(グループの個数-1)
"""
import sys
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
s = input()

score = 0
for i in range(n-1):
    if s[i] == s[i+1]: score += 1

ans = min(score+2*k, n-1)
print(ans)