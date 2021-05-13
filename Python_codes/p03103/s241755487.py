n,m = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(n)]
AB.sort()

cost = 0
for i in range(n):
  if m <= AB[i][1]:
    cost += m * AB[i][0]
    print(cost)
    exit()
  else:
    m = m - AB[i][1]
    cost += AB[i][1] * AB[i][0]
    
print(cost)