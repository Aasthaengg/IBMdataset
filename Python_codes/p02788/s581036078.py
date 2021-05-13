(N,D,A) = map(int,input().split())
l = []
for i in range(N):
    l.append([int(x) for x in input().split()])
l.sort()
k = [0 for i in range(N)]
for i in range(N):
    k[i] = -((-l[i][1])//A)

m = [0] * N
ub = 0
cnt = 1
for i in range(N):
    if ub < N-1:
        while l[ub + 1][0]-l[i][0] <= 2*D:
            cnt += 1
            ub += 1
            if ub == N - 1:
                break
        m[i] = cnt
    else:
        m[i] = cnt
    cnt -= 1

ans = 0
al = 0
s = [0 for i in range(N)]
j = 0
for i in range(N):
    s[i] = max(k[i]-al,0)
    ans += s[i]
    al += s[i]
    if i < N-1:
        while j+m[j]-1 < i+1:
            al -= s[j]
            if j < N-1:
                j += 1

print(ans)