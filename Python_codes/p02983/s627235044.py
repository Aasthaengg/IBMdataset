l,r = map(int,input().split())

ans = 2018
for i in range(l,l+2019):
    for j in range(i+1,min(r+1,i+2019)):
        ans = min(ans,(i*j)%2019)
print(ans)