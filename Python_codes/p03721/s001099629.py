num=[]
n,k=map(int,input().split())
for i in range(n):
    num.append(list(map(int,input().split())))
str= lambda val: val[0]
num.sort(key=str)
num1=0
for i in range(n):
    num1+=num[i][1]
    if num1>=k:
        ans=num[i][0]
        break
print(ans)
