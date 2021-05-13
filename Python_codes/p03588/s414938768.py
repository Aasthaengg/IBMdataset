n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))


a.sort()
ans=0
ans=a[n-1][0]+a[n-1][1]
print(ans)

