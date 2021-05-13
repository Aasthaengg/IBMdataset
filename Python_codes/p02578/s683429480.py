N = int(input())
A = list(map(int, input().split()))
i = 0
d = 0
s = 0
while (i < N-1):
    A[i] = A[i] + d
    if (A[i] > A[i+1]):
        d = A[i] - A[i+1]
        s = s + d
    else:
        d = 0
    i += 1
print(s)