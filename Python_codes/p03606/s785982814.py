N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    l,r = A[i]
    cnt += r-l+1
print(cnt)