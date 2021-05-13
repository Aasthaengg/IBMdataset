N,M = map(int,input().split())
A = list(map(int,input().split()))
su = sum(A)
l = []

for i in range(N):
    for j in range(30):
        l += -(-A[i]//2),
        A[i] //= 2

l.sort(reverse=True)

print(su - sum(l[:M]))