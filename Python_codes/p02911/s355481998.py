def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, K, Q = MI()
A = [K - Q] * N

for i in range(Q):
    A_i = INT()
    A[A_i - 1] += 1
    
for a in A:
    print("Yes" if a > 0 else "No")