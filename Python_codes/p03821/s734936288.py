n=int(input())
a=[]
b=[]
for i in range(n):
    na,nb=map(int,input().split())
    a.append(na)
    b.append(nb)
ans=0
num=0
for i in range(n):
    num1=(num+a[-i-1])%b[-1-i]
    if num1!=0:
        num+=b[-1-i]-num1
        ans+=b[-1-i]-num1
print(ans)
