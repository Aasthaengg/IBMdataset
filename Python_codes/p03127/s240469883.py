N = int(input())
A = sorted([int(i) for i in input().split()])

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

ans = A[0]
for i in range(1, N):
    ans = gcd(ans, A[i])

print(ans)