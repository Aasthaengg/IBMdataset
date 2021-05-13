n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(1,n):
    minp = min(p[i-1:i+2])
    maxp = max(p[i-1:i+2])
    if p[i] != minp and p[i] != maxp:
        cnt += 1

print(cnt)