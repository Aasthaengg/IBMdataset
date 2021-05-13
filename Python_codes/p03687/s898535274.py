INF = int(1e9+7)
s = input()
d = list('abcdefghijklmnopqrstuvwxyz')
ans = INF
for i in d:
    lis = [-1]
    for j in range(len(s)):
        if s[j] == i:
            lis.append(j)
    lis.append(len(s))
    val = 0
    for j in range(1,len(lis)):
        val = max(val,lis[j]-lis[j-1]-1)
    ans = min(ans,val)
print(ans)
