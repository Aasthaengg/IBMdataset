N = int(input())
st = [list(input().split()) for _ in range(N)]
X = input()

ans = 0
I = []
for i in range(N):
  if st[i][0] != X and len(I) == 0:
    continue
  elif st[i][0] == X:
    I.append(i)
  else:
    ans += int(st[i][1])
print(ans)