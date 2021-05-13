import sys,bisect,math
input = sys.stdin.readline

N,C,K = list(map(int,input().split()))
T = sorted([int(input()) for i in range(N)])

n = 0
cnt = 0
while n < N:
    target = T[n]+K
    nb = n
    n = bisect.bisect_right(T,target)
    if n - nb > C:
        n = nb + C
    cnt += 1
print(cnt)
