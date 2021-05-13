n=int(input())
num=[]
for i in range(n):
    x,l=map(int,input().split())
    num.append([x,l,x+l])
str1= lambda val: val[2]
num.sort(key=str1)
ans=n
num1=num[0][2]
for i in range(n-1):
    if num1>num[i+1][0]-num[i+1][1]:
        ans-=1
    else:
        num1=num[i+1][2]
print(ans)
