# coding: utf-8
N, h, w = map(int,input().split())
#N = int(input())
#l = list(map(int,input().split()))
#s = list(map(str,input().split()))
ans = 0
for i in range(N):
    a, b = map(int,input().split())
    if a >= h and b >= w:
        ans += 1

print(ans)