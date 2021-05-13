N = int(input())
A = list(map(int, input().split()))

c = 1; w = 0
for i in range(N-1):
    if w == 0:
        if A[i] < A[i+1]:
            w = 1
        elif A[i] > A[i+1]:
            w = -1
    elif (w > 0 and A[i] > A[i+1]) or (w < 0 and A[i] < A[i+1]):
         w = 0
         c += 1

print(c)
