N = int(input())
musics = []
for _ in range(N):
  s, t = input().split()
  musics.append([s, int(t)])
x = input()
passed = False
ans = 0
for i in range(N):
  if passed: ans += musics[i][1]
  if x == musics[i][0]: passed = True
print(ans)