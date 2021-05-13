n=int(input())
p=list(map(int,input().split()))
num1=0
num=[]
for i in range(1,n+1):
    if p[i-1]==i:
        num1+=1
    else:
        if num1!=0:
            num.append(num1)
            num1=0
if num1!=0:
    num.append(num1)
ans=0
for i in range(len(num)):
    ans+=-(num[i]//-2)
print(ans)
