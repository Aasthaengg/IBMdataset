import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))

a, b = max(A), min(A)
for t in [a, b]:
    for i in range(len(A)):
        if A[i] == t:
            A.pop(i)
            break

ans = a-b
for i in range(n-2):
    ans += abs(A[i])
print(ans)

for i in range(n-2):
    if A[i] > 0:
        print(b, A[i])
        b -= A[i]
    else:
        print(a, A[i])
        a -= A[i]
print(a, b)