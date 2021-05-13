n = int(input())
p = list(map(int,input().split()))

ps = sorted(p)

cnt = 0
for i in range(len(p)):
  if p[i] != ps[i] :
    cnt += 1
    if cnt > 2 :
      print("NO")
      exit()

print("YES")

