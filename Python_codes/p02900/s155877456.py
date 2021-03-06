def factorization(n):
    arr = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if arr=={}:
        arr[n] = 1

    return arr


a, b = map(int, input().split()) 
a_fac = factorization(a)
b_fac = factorization(b)
lcm = {}
for prime,cnt in a_fac.items():
    if prime in b_fac and prime != 1:
        lcm[prime] = min(cnt, b_fac[prime])

print(len(lcm)+1)