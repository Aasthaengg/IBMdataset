n,k = map(int,input().split())
a = list(map(int,input().split()))
l = [[0,0] for _ in range(40)]
for i in range(n):
    for j in range(40):
        l[j][a[i] >> j & 1] += 1
lst = [0]*41
for i in range(40):
    lst[i+1] = lst[i] + max(l[i])*2**i
l2 = [k >> j & 1 for j in range(40)]
lst2 = [0]*41
for i in range(39,-1,-1):
    lst2[i] = lst2[i+1]+l[i][1-l2[i]]*(2**i)
ans = lst2[0]
for i in range(40):
    if l2[i] == 0:
        continue
    t = lst2[i+1] + l[i][1]*(2**i) + lst[i]
    ans = max(t,ans)
print(ans)