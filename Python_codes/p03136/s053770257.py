N = int(input())
*A, = map(int, input().split())
m = max(A)
if 2*m < sum(A):
    print('Yes')
else:
    print('No')