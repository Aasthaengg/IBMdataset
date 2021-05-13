# coding: utf-8

N = int(input())
alp = [chr(i) for i in range(97, 97+26)]
L = []
for i in range(N):
    s = list(input())
    L.append(s)
for i in range(N):
    L[i].sort()
L.sort()

ans = 0
cnt = 1
for i in range(N-1):
    if L[i]==L[i+1]:
        cnt += 1
    else:
        ans += cnt*(cnt-1)//2
        cnt = 1
if cnt > 1:
    ans += cnt*(cnt-1)//2
print(ans)