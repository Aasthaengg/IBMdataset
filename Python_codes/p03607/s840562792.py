n=int(input())
num=[]
def ap(num1):
    num.append(num1)
for i in range(n):
    a=int(input())
    ap(a)
num.sort()
num1=num[0]
num2=1
ans=0
for i in range(n-1):
    if num[i+1]==num1:
        num2+=1
    else:
        num1=num[i+1]
        if num2%2==1:
            ans+=1
        num2=1
if num2%2==1:
    ans+=1
print(ans)
