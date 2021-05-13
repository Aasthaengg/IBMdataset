n=int(input())
a=list(map(int,input().split()))

s=0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        a[i+1]=str(a[i])
        s+=1
print(s)