n = int(input())
musics = [list(map(str, input().split())) for _ in range(n)]
x = input()

ans = 0
flag = False
for i in range(n):
  if flag:
    ans += int(musics[i][1])
  if musics[i][0] == x:
    flag = True

print(ans)