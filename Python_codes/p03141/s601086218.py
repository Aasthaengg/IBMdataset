n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]

a_b=[]
x=0
for a,b in ab:
    a_b.append(a+b)
    x-=b
a_b.sort(reverse=True)
ans=0
for i in range(0,n,2):
    ans+=a_b[i]

print(ans+x)