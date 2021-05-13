n,m = map(int,input().split())
l = [[] for i in range(8)]

for i in range(n):
    l1 = list(map(int,input().split()))

    for j in range(8):
        check = 0
        for k in range(3):
            if (j >> k ) & 1:
                check += l1[k]
            else:
                check -= l1[k]
        l[j].append(check)

ans = 0
for i in l:
    i.sort(reverse=True)
    check = sum(i[:m])
    ans = max(ans,check)
print(ans)
