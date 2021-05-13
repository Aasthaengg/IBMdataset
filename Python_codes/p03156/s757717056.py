N = int(input())
A, B = list(map(int, input().split()))
P = list(map(int, input().split()))

a = sum(p <= A for p in P)
b = sum(A < p <= B for p in P)
c = sum(B < p for p in P)

print(min(a, b, c))