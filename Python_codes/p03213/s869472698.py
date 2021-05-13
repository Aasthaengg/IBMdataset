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


n = int(input())
cnt = [0]*101
ans=0

for i in range(1,n+1):
  lst = factorization(i)
  for j in lst:
    cnt[j[0]]+=j[1]

a,b,c,d,e=0,0,0,0,0

for i in cnt:
  if 2<=i<=3:
    a+=1
  elif 4<=i<=13:
    b+=1
  elif 14<=i<=23:
    c+=1
  elif 24<=i<=73:
    d+=1
  elif 74<=i:
    e+=1


ans+=e
ans+=(d+e)*(a+b+c+d+e-1)
ans+=(c+d+e)*(b+c+d+e-1)
ans+=(b+c+d+e)*(b+c+d+e-1)*(a+b+c+d+e-2)//2


print(ans)