from math import factorial
n, m = map(int, input().split())
mod = 10**9 + 7

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1+1)):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    # if arr==[]:
    #     arr.append([n, 1])

    return arr

arr = factorization(m)
if not arr:
    print(1)
    exit()
ans = 1
for a, b in arr:
    pattern = factorial(b+n-1) // (factorial(b) * factorial(n-1))
    ans = (ans * pattern)%mod

print(ans)