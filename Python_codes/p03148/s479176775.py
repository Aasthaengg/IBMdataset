N,K = map(int,input().split())
td = [list(map(int,input().split())) for _ in range(N)]
td.sort(key=lambda x:-x[1])
l,r = td[:K],td[K:]
used_l = [0]*N
for i in range(K):
    used_l[l[i][0]-1] += 1

remove = []
for i in range(K-1,-1,-1):
    if used_l[l[i][0]-1] >= 2:
        remove.append(l[i][1])
        used_l[l[i][0]-1] -= 1

used_r = used_l.copy()
add = []
for i in range(N-K):
    if used_r[r[i][0]-1] == 0:
        add.append(r[i][1])
        used_r[r[i][0]-1] += 1

t = sum(used_l)

ans = t**2
for i in range(K):
    ans += l[i][1]

ref = ans
for i in range(min(len(remove),len(add))):
    ref += (t+1)**2-t**2+add[i]-remove[i]
    t += 1
    ans = max(ans,ref)

print(ans)