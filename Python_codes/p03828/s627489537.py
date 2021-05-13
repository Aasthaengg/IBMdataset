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


n=int(input())
mod=10**9+7

lst=[0]*1000

for i in range(2,n+1):
  x=factorization(i)
  for j in x:
    lst[j[0]]+=j[1]
    
ans=1

for i in lst:
  ans*=(i+1)
  ans%=mod
  
print(ans)