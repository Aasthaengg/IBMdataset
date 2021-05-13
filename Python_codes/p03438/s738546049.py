n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_gap = 0
b_gap = 0
for i in range(n):
    if A[i]>B[i]:
        a_gap+=A[i]-B[i]
    if A[i]<B[i]:
        b_gap+=(B[i]-A[i])//2

if b_gap-a_gap<0:
    print('No')
else:
    print('Yes')