N = int(input())
A = [int(s) for s in input().split()]

A.sort(reverse=True)

Alice = 0
Bob = 0
for i, a in enumerate(A):
    if i % 2 == 0:
        Alice += a
    else:
        Bob += a
ans = Alice - Bob

print(ans)