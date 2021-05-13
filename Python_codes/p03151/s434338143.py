n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
D=[i-j for i,j in zip(a,b)]
c=[i for i in D if i>0]
c.sort()
d=[i for i in D if i<0]

e=sum(d)
if sum(a)<sum(b):
    print(-1)
elif len(d)==0:
    print(0)
else:
    ans=0
    for i in c[::-1]:
        ans+=1
        e+=i
        if e>=0:
            print(ans+len(d))
            exit()