n,k = map(int,input().split())
x = list(map(int,input().split()))
flag = True
for i in range(n+1):
    if i == n or x[i] > 0:
        x.insert(i,0)
        zahyou = i
        break
ans = 10**18
for i in range(k+1):
    flag = True
    if zahyou + i < n+1 and zahyou -k+i >= 0:
        mainasu = x[zahyou]-x[zahyou-k+i]
        purasu = x[zahyou+i]-x[zahyou]
        if mainasu != 0 and purasu != 0:
            purasu += min(mainasu,purasu)
        ans = min(ans,mainasu+purasu)
print(ans)
