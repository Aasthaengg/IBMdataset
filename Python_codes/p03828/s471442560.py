n=int(input())
mod=10**9+7
ans=[0]*(1000+1)
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

for i in range(1000+1):
  for j in factorization(i):
    ans[j[0]]+=j[1]
  if n==i:
    break
anss=1
for i in range(2,len(ans)):
  anss*=(ans[i]+1)%mod
  anss%=mod
print(anss)
