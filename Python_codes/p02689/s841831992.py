N, M = map(int, input().split())
H = list(map(int, input().split()))
Root = []
for i in range(M):
  temp = list(map(int, input().split()))
  Root.append(temp)

ans = [1]*N

for i in range(M):
  r_start = Root[i][0] - 1 
  r_stop = Root[i][1] - 1
  if H[r_start] < H[r_stop]:
    ans[r_start] = 0
  elif H[r_start] == H[r_stop]:
    ans[r_start] = 0
    ans[r_stop] = 0
  else:
    ans[r_stop] = 0

print(sum(ans))