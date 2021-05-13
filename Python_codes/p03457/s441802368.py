N = int(input())
T = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
normal = True
def judge(a, b):
  m = b[0]-a[0]-abs(b[1]-a[1])-abs(b[2]-a[2])
  if m>=0 and m%2==0:
    return True
  else:
    return False
for i in range(N):
  if judge(T[i], T[i+1]):
    pass
  else:
    normal = False
    break
print("Yes" if normal else "No")