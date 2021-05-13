N, X = map(int, input().split())
L = list(map(int, input().split()))
D = 0
A = 0
if D <= X:
    A += 1
for i in L:
    D += i
    if D <= X:
        A += 1
print(A)