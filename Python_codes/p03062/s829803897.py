import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
cnt = 0

for Ai in A:
    if Ai<0:
        cnt += 1

if cnt%2==0:
    print(sum(abs(Ai) for Ai in A))
else:
    A.sort(key=lambda x: abs(x))
    print(-abs(A[0])+sum(abs(Ai) for Ai in A[1:]))