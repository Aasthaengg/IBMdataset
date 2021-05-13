import math

def combi(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, p = map(int, input().split())
L = list(map(int, input().split()))
odd = 0
even = 0
for a in L:
    if a % 2:
        odd += 1
    else:
        even += 1
c = 0
if p == 0:
    for i in range(0, odd + 1, 2):
        c += combi(odd, i)
else:
    for i in range(1, odd + 1, 2):
        c += combi(odd, i)
ans = 2 ** even * c
print(ans)
