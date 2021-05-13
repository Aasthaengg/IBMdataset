N=int(input())
a=list(set(list(map(int,input().split()))))
ans=0
a.sort()
for i in range(1,len(a)):
    ans+=a[i]-a[i-1]
print(ans)