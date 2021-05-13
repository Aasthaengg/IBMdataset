n = int(input())
A = list(map(int, input().split()))
c = 1000  # cash
s = 0  # stock
up = False
for i in range(n-1):
    if A[i] < A[i+1]:
        if not up:
            s, c = divmod(c, A[i])
            up = True
            #print(A[i], c, s)
    elif A[i] > A[i+1]:
        if up:
            c += s * A[i]
            s = 0
            up = False
            #print(A[i], c, s)
    else:
        pass
else:
    c += s * A[-1]
print(c)