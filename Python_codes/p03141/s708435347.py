from collections import deque
N = int(input())
lis = []

A = []
B = []
for i in range(N):
    Ain,Bin = map(int,input().split())
    A.append(Ain)
    B.append(Bin)
    lis.append((Ain+Bin,i))
lis.sort()
lis.reverse()
lis = deque(lis)

takacnt = 0
aocnt = 0

# print(taka)
# print(ao)

for i in range(N):
    if i % 2 == 0:
        val = lis.popleft()
        takacnt += A[val[1]]
    else:
        val = lis.popleft()
        aocnt += B[val[1]]
print(takacnt-aocnt)
