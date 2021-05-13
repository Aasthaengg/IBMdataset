import bisect
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
ans = 0
b = []
for i in range(N):
    b.append(N - bisect.bisect_left(C,B[i]+1))
b.append(0)
for i in range(N-1,-1,-1):
    b[i] += b[i+1]
ans = 0
for i in range(N):
    ans += b[bisect.bisect_left(B, A[i]+1)]
print(ans)