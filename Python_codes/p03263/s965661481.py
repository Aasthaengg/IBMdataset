h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
d = [[0]*w for _ in range(h)]
def nxt(i,j):
  if i%2 == 0 and j == w-1:
    return i+1,j
  elif i%2 == 1 and j == 0:
    return i+1,j
  elif i%2 == 0:
    return i,j+1
  else:
    return i,j-1
i,j = 0,0
cnt = 0
ans = []
while True:
  k,l = nxt(i,j)
  if k == h:
    break
  if a[i][j] % 2 == 1:
    cnt += 1
    a[k][l] += 1
    ans.append([i+1,j+1,k+1,l+1])
  i,j = k,l
print(cnt)
for l in ans:
  print(*l)