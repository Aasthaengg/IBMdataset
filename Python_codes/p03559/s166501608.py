import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
A = A[:N]
B = list(map(int,input().split()))
B = B[:N]
C = list(map(int,input().split()))
C = C[:N]

A.sort()
B.sort()
C.sort()

ans = 0

#B_iを選んだ時にAの選び方は何通り？
BB = [0] * N
a = 0
for b in range(N):
    while A[a] < B[b] and a <= N-2:
        a += 1
    if a == N-1 and A[a] < B[b]:
        BB[b] = N
    else:
        BB[b] = a
#print(BB)

Bsum = [0] * N
Bsum[0] = BB[0]
for bb in range(1,N):
    Bsum[bb] = Bsum[bb-1] + BB[bb]
#print(Bsum)

ans = 0
b_ = 0
for c in range(N):
    while B[b_] < C[c] and b_ <= N-2:
        b_ += 1
    if b_ == N-1 and B[b_] < C[c]:
        b_ += 1
    b_ -= 1
    if b_ == -1:
        b_ = 0
        continue
    #print(b_)
    ans += Bsum[b_]

print(ans)