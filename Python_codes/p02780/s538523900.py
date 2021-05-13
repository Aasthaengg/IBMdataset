N,K  = map(int,input().split())
p = list(map(int,input().split()))

dice = []
for i in range(N):
  temp = (1+p[i])/2
  dice.append(temp)

#print(dice)
ans = 0
prev = sum(dice[:K])
ans = prev
for i in range(K,N):
  temp = prev-dice[i-K]+dice[i]
  ans = max(ans,temp)
  prev = temp
print(ans)
