N,X = map(int,input().split())
L = list(map(int,input().split()))
L.append(0)
D,i,cnt = 0,0,0
while(D <= X and cnt <= N):
  D = D + L[i]
  cnt +=1
  i += 1
print(cnt)