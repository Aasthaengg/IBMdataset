import sys
input = sys.stdin.readline
N, K, Q = map(int, input().split())
A = [int(input().rstrip()) for i in range(Q)]
#print(A)
score =[0]*(N)


for i in range(Q):
    score[A[i]-1] += 1
#print(score)

for i in range(N):
    if K+score[i]-Q >0:
        print('Yes')
    else:
        print('No')