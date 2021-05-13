N = int(input())
A = list(map(int, input().split()))

d = [0]*N
d[0] = 1000
for i in range(1, N):
    if A[i-1] < A[i]:
        d[i] = d[i-1]+(d[i-1]//A[i-1])*(A[i]-A[i-1])
    else:
        d[i] = d[i-1]
print(d[-1])
