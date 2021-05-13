n,m = map(int,input().split())
h =  list(map(int,input().split()))

goto = [[0] for _ in range(n)]

cnt = 0

for i in range(m):
    a,b = map(int,input().split())
    goto[a-1] += [h[b-1]]
    goto[b-1] += [h[a-1]]

for j in range(n):
    if max(goto[j])< h[j]:
        cnt += 1

print(cnt)
