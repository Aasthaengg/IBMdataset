MOD=10**9+7
x , y = map(int, input().split())
a=(2*x-y)//3
b=(2*y-x)//3
if 2*a+b!=x:
    print(0)
    exit()

factorial = [1]
inverse = [1]

n=a+b
r=a

for i in range(1, n+2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))

def combi(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD

ans = combi(n,r)
print(ans)
