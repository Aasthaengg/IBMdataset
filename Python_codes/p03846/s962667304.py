n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)
# aがあるべきパターンになってるかチェック
if n % 2 == 1:
  del(a[-1])
r = 1
turn = 0
start = n - 1
check = True

for i in range(0, len(a)):
  turn += 1  
  if a[i] != start:
    r = 0
  if turn > 1:    
    turn = 0
    start -= 2

if not r:
  print(0)
else:
  # aがあるべきパターンならありうる組み合わせの数を計算
  r = 2**(n//2) % (10**9 + 7)
  print(r)

  
