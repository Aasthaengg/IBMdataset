n, k = map(int, input().split())
A = sorted(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


smallest_ball = A[0]
for a in A[1:]:
    smallest_ball = gcd(smallest_ball, a)

print("POSSIBLE" if (A[-1]-k) %
      smallest_ball == 0 and k <= A[-1] else "IMPOSSIBLE")