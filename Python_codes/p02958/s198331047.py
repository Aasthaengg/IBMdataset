N = int(input())
P = list(map(int, input().split()))

s = 0
A = [i for i in range(1, N+1)]

for i in range(N):
    if P[i] != A[i]:
        s += 1
        
print('NO' if s > 2 else 'YES')