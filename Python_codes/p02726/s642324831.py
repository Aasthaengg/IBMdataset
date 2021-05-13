N,X,Y = map(int,input().split())
X -= 1
Y -= 1
aggre= [0] * (N - 1)

for i in range(N):
  for j in range(N):
    if i == j:
      continue
    dist = min(abs(j - i),abs(X - i) + abs(Y - j) + 1,abs(Y - i) + abs(X - j) + 1)
    #if dist >= N // 2:
      #print("dist i j",dist,i,j)
    aggre[dist - 1] += 1
    
#ans = [i // 2 for i in aggre]
for a in aggre:
  print(a // 2)