N,K = map(int,input().split())

A = set()

for _ in range(K):
    input()
    A |= set(input().split())

print(N - len(A))