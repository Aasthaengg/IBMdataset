from itertools import accumulate
N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
acc1 = list(accumulate(A[0], lambda x,y:x+y))
acc2 = [0]+list(accumulate(A[1], lambda x,y:x+y))
ma = -1
for i in range(N):
    ma = max(ma, acc2[-1]-acc2[i]+acc1[i])
print(ma)