n=int(input())
a=list(map(int,input().split()))
num=[0]*n
ans=0
for i in range(n):
    num[a[i]-1]+=1
def cul(num1):
    if num1>=2:
        return ((num1-1)*num1)//2
    else:
        return 0
for i in range(n):
    ans=ans+cul(num[i])
for i in range(n):
    print(ans-num[a[i]-1]+1)
