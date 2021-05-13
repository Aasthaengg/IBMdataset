import math

N, M  = map(int, input().split())

MOD = 10**9+7

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

fact = factorization(M)

ans = 1
if M == 1:
  print(1)

else:


  for i in range(len(fact)):
    ans *= ( math.factorial(N-1+fact[i][1]) ) // ( (math.factorial(N-1)) * (math.factorial(fact[i][1])) ) % MOD
    ans = ans%MOD

  print(ans)
