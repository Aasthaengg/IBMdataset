n=int(input())
plus=[input() for _ in range(n)]
m=int(input())
minus=[input() for _ in range(m)]
res=[]
for i in plus:
    a=plus.count(i)
    b=minus.count(i)
    res+=[(a-b,i)]
res.sort(reverse=1)
print(max(0,res[0][0]))