import sys
readline = sys.stdin.buffer.readline

A, B = list(map(int, readline().split()))

def gcd(a,b):
    while b > 0:
        a, b = b, a % b

    return a

ans = A * B // gcd(A, B)
print(ans)
