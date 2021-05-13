n=int(input())
a=list(map(int,input().split()))
a.sort()
count=1
ans=0
ans=a[len(a)-1]*count
count+=1
for i in a:
    if ans%i!=0:
        break
ans2=0
for i in a :
    ans2+=ans/i
    
print (ans/ans2)