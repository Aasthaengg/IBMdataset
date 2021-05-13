N,M = map(int,input().split())
cnt = [0]*(N+10)
for i in range(M):
    a,b = map(int,input().split())
    cnt[a]+=1
    cnt[b]+=1

for c in cnt:
    if c%2 == 1:
        print('NO')
        import sys
        sys.exit()
print('YES')
