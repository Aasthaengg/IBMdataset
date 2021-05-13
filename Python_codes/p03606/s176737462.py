N = int(input())
cnt = 0

for i in range(0,N):
  R, L = list(map(int,input().split()))
  cnt = cnt + L - R + 1
print(cnt)