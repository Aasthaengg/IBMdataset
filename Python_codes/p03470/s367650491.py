N = int(input())
d = [int(input()) for _ in range(N)]

# 重複を除いた要素数を数えるために、setを使う以外にバケット法による方法がある
l = [0]*100
for i in range(N):
  l[d[i]-1] = 1
  
print(sum(l))