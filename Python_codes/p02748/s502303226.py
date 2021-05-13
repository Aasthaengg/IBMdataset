A,B,M = map(int,input().split())
a_price = list(map(int,input().split()))
b_price = list(map(int,input().split()))

dis = []
for _ in range(M):
  dis.append(list(map(int,input().split())))

total = min(a_price)+min(b_price)

dis_total = []
for k in range(M):
  dis_total.append(a_price[dis[k][0]-1]+b_price[dis[k][1]-1]-dis[k][2])

if total <= min(dis_total):
  print(total)
else:
  print(min(dis_total))