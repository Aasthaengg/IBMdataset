N = int(input())
A = list(map(int, input().split()))
c = 0
k = 0
for i in range(N):
    if A[i] < 0:
        c += 1
        A[i] *= -1
    elif A[i] == 0:
        k = 1

if c % 2 == 0:
    print(sum(A))
elif k == 1:
    print(sum(A))
else:
    print(sum(A)-2*min(A))