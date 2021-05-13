n,y = map(int,input().split())
ans = '-1 -1 -1'
for i in range(n+1):
    for j in range(n+1-i):
        k = n - i - j
        if (i*1000 + j*5000 + k*10000) == y:
            ans = str(k) + ' ' + str(j) + ' ' + str(i)
            break
print(ans)