n = int(input())
A = list(map(int,input().split()))

minus = 0
zero = 0

for i in range(n):
    if A[i] < 0:
        minus += 1
    elif A[i] == 0:
        zero += 1

A2 = [abs(i) for i in A]
if minus %2 == 0 or zero >= 1:
    print(sum(A2))
else:
    print(sum(A2)-2*min(A2))