n=int(input())
num=[]
a=[]
b=[]
for i in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
    num.append([A,B,A+B])
ansa=sum(a)
ansb=sum(b)
num.sort(key=lambda x: x[2],reverse=True)
for i in range(n):
    if i%2==0:
        ansb-=num[i][1]
    else:
        ansa-=num[i][0]
print(ansa-ansb)
