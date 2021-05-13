N, T = map(int, input().split())
A = list(map(int, input().split()))
#全て同じではない

#buy = int(T / 2)
#一番安い町で買って、高い町で売る
now = 10 ** 10
max_sub = 0
count = 1
for i in range(N):
  bb = A[i] - now
  if bb > max_sub:
    max_sub = bb
    count = 1
  elif bb == max_sub:
    count += 1

  now = min(now, A[i])
  #print(bb, max_sub, now, count)
  
#print(max_sub, count)
print(count)    
