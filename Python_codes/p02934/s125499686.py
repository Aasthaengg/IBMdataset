N = int(input())
A = list(map(int, input().split()))

b = 1
for a in A:
    b *= a

C = [1 for _ in range(N)]
for i, a in enumerate(A):
    C[i] = b//a

print(b/sum(C))