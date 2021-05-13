import math

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
total = sum(B) - sum(A)
cnt1, cnt2 = 0,0

for i in range(n):
    if A[i] > B[i]:
        cnt1 += A[i] - B[i]
    elif A[i] < B[i]:
        cnt2 += math.ceil((B[i]-A[i])/2)

if max(cnt1, cnt2) <= total:
    print('Yes')
else:
    print('No')