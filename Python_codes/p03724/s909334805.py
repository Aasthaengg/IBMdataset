N,M = map(int,input().split())
k = 0
while True:
    if 2**k>=N:
        break
    k += 1
A = [0 for i in range(2**k+1)]
for _ in range(M):
    a,b = map(int,input().split())
    if b<a:
        a,b = b,a
    A[a] += 1
    A[b] -= 1
B = [0 for i in range(2**k+2)]
for i in range(2**k+1):
    B[i+1] = B[i]+A[i]
flag = 0
for i in range(2**k+1):
    if B[i]%2==1:
        flag = 1
        break
if flag==0:
    print("YES")
else:
    print("NO")