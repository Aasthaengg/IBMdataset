n = int(input())
l = list(map(str,input()))

ans = 0
for i in range(n):
    a = l[:i]
    b = l[i:]
    tmp = []
    for j in a:
        if j in b:
            tmp.append(j)
    tmp = set(tmp)
    ans = (max(ans,len(tmp)))

print(ans)