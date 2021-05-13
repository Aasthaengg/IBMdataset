n = int(input())

a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

ans = 0
for i in range(n-1,-1,-1):
    if (a[i]+ans)%b[i] == 0:
        pass
    elif a[i] + ans > b[i]:
        ans += b[i]-((a[i]+ans)%b[i])
    else:
        ans += b[i]-(a[i]+ans)  
print(ans)
