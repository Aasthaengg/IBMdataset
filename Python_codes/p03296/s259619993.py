N=int(input())
a=list(map(int,input().split()))
t=c=0
s=0
for i in a:
    if i==t:
        c+=1
    else:
        t=i
        s+=c//2
        c=1
print(s+c//2)