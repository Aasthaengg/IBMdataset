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
############################  
from math import floor

N=int(input())
p= floor(N**0.5)

ans=0
for i in range(1,p+1):
  if N%i==0:
    s = i
    t = N//i-1
    #print(s,t)
    u = N//i
    v = i-1
    #print(u,v)
    if s<t:
      ans += t
    if u<v:
      ans += v
print(ans)