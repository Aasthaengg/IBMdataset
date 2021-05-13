#素因数分解
#factorization(2016)=[[2, 5], [3, 2], [7, 1]]の形で出力
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int((n**0.5//1))+1):
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
p=10**9+7
fli=[1]*(n+1)
for i in range(2,n+1):
  f=factorization(i)
  for j in range(len(f)):
    fli[f[j][0]]+=f[j][1]
ans=1
for i in range(n+1):
  ans=ans*fli[i]%p
print(ans)