n,k=map(int,input().split())
a=list(map(int,input().split()))
num=[]
for i in range(n):
    num.append([a[i],i])
s1= lambda val: val[0]
num.sort(key=s1)
num1=0
num[0].append(0)
for i in range(1,n):
    if num[i][0]==num[i-1][0]:
        num[i].append(num1)
    else:
        num1=i
        num[i].append(num1)
num2=0
num3=0
s2=lambda val: val[1]
num.sort(key=s2)
for i in range(n):
    num2+=num[i][2]
    for j in range(i):
        if num[i][0]>num[j][0]:
            num3+=1
ans=((num2-num3)*k)%(10**9+7)
ans+=(num2*((((k-1)*k)//2)%(10**9+7)))%(10**9+7)
print(ans%(10**9+7))
