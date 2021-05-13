n, k = map(int, input().split())
A = set([])

for i in range(k):
    d = input()
    A = A | set(map(int, input().split()))

print(n-len(A))