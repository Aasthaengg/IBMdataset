n , k = map(int,input().split())
hoge = [list(map(int,input().split())) for _ in range(n)]
hoge.sort()
sushi = 0
for i in range(n):
  sushi += hoge[i][1]
  if sushi >= k:
    print(hoge[i][0])
    break