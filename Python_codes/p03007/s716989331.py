N = int(input())
A = list(map(int, input().split()))
A.sort()
a = A[0]
b = A[-1]
xy = []
for i in range(1, N-1):
    if A[i] > 0:
        xy.append((a, A[i]))
        a -= A[i]
    else:
        xy.append((b, A[i]))
        b -= A[i]
xy.append((b, a))
print(b-a)
for x, y in xy:
    print(x, y)