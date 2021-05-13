N,M = map(int,input().split())

si = N
ans = 0

while(si <= M):
    ans += 1
    si = si * 2

print(ans)