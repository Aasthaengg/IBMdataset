N = int(input())
A = list(map(int, input().split()))

l = [0]*N
l[0] = A[0]
r = [0]*N
r[-1] = A[-1]
for i in range(1, N):
    l[i] = l[i-1]+A[i]
    r[N-i-1] = r[N-i]+A[N-i-1]

res = 10**10
for i in range(N-1):
    res = min(abs(l[i]-r[i+1]), res)

print(res)