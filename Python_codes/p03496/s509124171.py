N = int(input())
A = [int(a) for a in input().split()]
ma = -1
mai = -1
for i in range(N):
    if abs(A[i]) > ma:
        ma = abs(A[i])
        mai = i

print(2*N-1)
for i in range(N):
    print(mai+1, i+1)
if A[mai] > 0:
    for i in range(N-1):
        print(i+1, i+2)
else:
    for i in range(N-1)[::-1]:
        print(i+2, i+1)