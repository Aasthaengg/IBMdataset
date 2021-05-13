from bisect import bisect_right
N,C,K = map(int,input().split())
T = sorted([int(input()) for _ in range(N)])
cur = 0
cnt = 0
while cur<N:
    ind = bisect_right(T,T[cur]+K)
    if ind-cur<=C:
        cnt += 1
        cur = ind
    else:
        cnt += 1
        cur += C
print(cnt)