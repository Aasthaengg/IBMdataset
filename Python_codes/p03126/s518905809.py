N,M = map(int,input().split())
foods = [0]*(M+1)
for i in range(N):
  line = list(map(int,input().split()))
  for j in range(1,line[0]+1):
    foods[line[j]]+=1
print(foods.count(N))