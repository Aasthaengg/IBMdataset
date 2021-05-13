n=int(input())
ans=0
temp=[0]*101

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
  
for i in range(1,n+1):
  a=factorization(i)
  for j in range(len(a)):
    temp[a[j][0]]=temp[a[j][0]]+a[j][1]
t75=0
t25=0
t15=0
t5=0
t3=0
t1=0
for i in range(n):
  if temp[i]>=74:
    t75=t75+1
  if temp[i]>=24:
    t25=t25+1
  if temp[i]>=14:
    t15=t15+1
  if temp[i]>=4:
    t5=t5+1
  if temp[i]>=2:
    t3=t3+1
  if temp[i]>=1:
    t1=t1+1
print(t75+t25*(t3-1)+t15*(t5-1)+t5*(t5-1)*(t3-2)//2)