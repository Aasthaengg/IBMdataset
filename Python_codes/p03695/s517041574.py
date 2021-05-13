n=int(input())
a=list(map(int,input().split()))
for i in range(n):a[i]=min(a[i],3200)//400
m=a.count(8)
s=set(a)
s.discard(8)
print(max(1,len(s)),len(s)+m)