k,a,b= map(int,input().split())
cur = 1
#交換しないほうがいい
if b - a <= 2:
  print(cur + k)
  exit()
#交換できない
if cur + k <= a+1:
  print(cur + k)
  exit()
#交換するまで増やす
cur, k, = a, k-a+cur
#偶数回交換する
cur += (b - a) * (k // 2)
k %= 2
#最後に足す
cur += k
print(cur)