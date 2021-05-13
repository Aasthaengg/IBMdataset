from math import factorial

def comb(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

n, p = map(int, input().split())
arr = list(map(int, input().split()))

odd = 0
even = 0
for a in arr:
    if a % 2 == 1:
        odd += 1
    else:
        even += 1

ans = 2 ** even
tmp = 0
for i in range(p, odd+1, 2):
    tmp += comb(odd, i)
ans *= tmp

print(ans)
