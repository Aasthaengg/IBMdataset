def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    MOD = 10 ** 9 + 7
    sm1 = [0] * n
    sm2 = [0] * n
    for i in range(n):
        now = a[i]
        for j in range(i+1,n):
            if now > a[j]:
                sm1[i] += 1
    for i in range(n):
        now = a[i]
        for j in range(i):
            if now > a[j]:
                sm2[i] += 1
    a1 = sum(sm1) % MOD
    d = (sum(sm2) + a1) % MOD

    ans = k * (2*a1 + (k-1)*d)
    ans %= MOD
    inv_2 = power_func(2,MOD-2,MOD)
    ans = ans *inv_2
    print(ans%MOD)

def power_func(a,n,m):
  bi=str(format(n,"b"))#2進表現に
  ans=1
  for i in range(len(bi)):
    ans=(ans*ans) %m
    if bi[i]=="1":
      ans=(ans*a) %m
  return ans

if __name__ == '__main__':
    main()
