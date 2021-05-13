def factorization(n):#素因数分解
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr
  

a,b=map(int,input().split())
al=factorization(a)
bl=factorization(b)

com=set(al) & set(bl)
if a==1 and b==1:
  print(1)
else:
  print(len(com)+1)
