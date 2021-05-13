n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
p=[]
m=[]
def app(num1):
    p.append(num1)
def apm(num2):
    m.append(num2)
if sum(a)<sum(b):
    ans=-1
else:
    for i in range(n):
        if a[i]>b[i]:
            app(a[i]-b[i])
        elif a[i]<b[i]:
            apm(b[i]-a[i])
    num=sum(m)
    ans=len(m)
    p.sort(reverse=True)
    num1=0
    for i in range(len(p)):
        if num1>=num:
            break
        num1+=p[i]
        ans+=1
        if num1>=num:
            break
print(ans)
