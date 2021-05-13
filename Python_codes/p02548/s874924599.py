import sys
n = int(sys.stdin.readline().strip())

# A * B + C, make sure A * B <= N, if A == B, it is (N-A*B) + 1, else ((N-A*B) + 1) * 2
res = 0
"""
for i in range(1, n//2+1):
    if i ** 2 < n:
        res += 1
    for j in range(i+1, n//i+1):
        if i*j >= n:
            break
        res +=  2

print(res)
"""

# A==B, from 1 to square root
res += int(n**0.5)
upperbound = int(n**0.5) + 1
if int(n**0.5) ** 2 == n:
    # n has int square root
    res -= 1
    upperbound = int(n**0.5)

# Assuming A < B
# A = 1, B=2...N-1
# A = 2, B=3...N/2 or N/2-1

for i in range(1, upperbound):
    if n % i == 0:
        half = n // i - 1 - i
    else:
        half = n//i - i
    res += half * 2
print(res)