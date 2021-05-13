n= int(input())
def fact_m(n, modulus=10**9+7):
    ans=1
    if n <= modulus//2:
        for i in range(1,n+1):
            ans = (ans * i) % modulus   
    else:
        for i in range(1,modulus-n):
            ans = (ans * i) % modulus
        ans = modinv(ans, modulus)

        if n % 2 == 0:
            ans = -1*ans + modulus
    return ans % modulus
print(fact_m(n))