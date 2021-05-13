n,m = map(int,input().split())

klist = []
slist = [list() for _ in range(m)]

for i in range(m):
    k,*s = map(int,input().split())
    klist.append(k)
    slist[i] = s

p = list(map(int,input().split()))

ans = 0
for i in range(2**n):
    for j in range(m):
        cnt = 0
        for l in slist[j]:
            if (i >> (l-1))&1 ==1:
                cnt += 1
        if cnt%2 != p[j]:
            break
    else:
        ans += 1

print(ans)
