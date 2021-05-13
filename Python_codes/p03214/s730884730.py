N = int(input())
A = list(map(int,input().split()))
a = sum(A)/N
ind = -1
dmin = 10**4
for i in range(N):
    if abs(a-A[i])<dmin:
        dmin = abs(a-A[i])
        ind = i
print(ind)