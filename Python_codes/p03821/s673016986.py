N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
for i in range(N-1,-1,-1):
    a = (-A[i][0]-cnt)%A[i][1]
    cnt += a
print(cnt)