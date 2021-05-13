A, B, K = map(int, input().split())

N = []

for i in range(K):
    if A + i < B:
        N.append(A + i)
    if B - i >= A:
        N.append(B - i)
    
for n in sorted(set(N)):
    print(n)