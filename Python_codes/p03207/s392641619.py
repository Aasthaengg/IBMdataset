# 初期入力
import sys
input = sys.stdin.readline
N = int(input())
p =[0]*N
for i in range(N):
    p[i] = int(input())
p.sort()
ans =sum(p[:-1]) +p[-1]//2
print(ans)