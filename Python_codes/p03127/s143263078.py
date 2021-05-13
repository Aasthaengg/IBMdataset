def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from math import gcd

N = INT()
A = LI()
A.sort()
ans = A[0]

all_can_div = True

for i in range(1, N):
    A[i] = gcd(A[i], ans)
    
    if A[i] != ans and all_can_div:
        all_can_div = False

print(ans if all_can_div else min(A))