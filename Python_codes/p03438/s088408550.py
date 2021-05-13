N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = sum(B)-sum(A)

one = 0
two = 0

for i in range(N):
    if A[i] > B[i]:
        one += A[i]-B[i]
    if A[i] < B[i]:
        two += (B[i]-A[i])//2
        if (B[i]-A[i])%2 == 1:
            one += 1

if one<=x and two<=x:
    print("Yes")
else:
    print("No")