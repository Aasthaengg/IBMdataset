from bisect import bisect_right
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
B1 = []
for i in range(N):
    ind = bisect_right(C,B[i])
    B1.append(ind)
B2 = [0 for _ in range(N+1)]
for i in range(N-1,-1,-1):
    B2[i] = B2[i+1]+N-B1[i]
cnt = 0
for i in range(N):
    ind = bisect_right(B,A[i])
    cnt += B2[ind]
print(cnt)