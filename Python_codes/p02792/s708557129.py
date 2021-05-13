n=int(input())
x=str(n)
keta=len(str(n))

l=[[0]*10 for i in range(10)]
for i in range(n+1):
    num=str(i)
    sento=int(num[0])
    matsubi=int(num[-1])
    if matsubi==0:
        continue
    l[sento][matsubi]+=1

sm=0
for i in range(n+1):
    num=str(i)
    sento=int(num[0])
    matsubi=int(num[-1])
    if matsubi==0:
        continue
    sm+=l[matsubi][sento]

print(sm)