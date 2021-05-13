n = int(input())
h = list(map(int, input().split()))

ans = 0
while max(h) != 0:
  if h[0] > 0: flag = True
  else: flag = False
    
  if flag:
    for i in range(n):
      if h[i] == 0: break
      h[i] -= 1
    ans += 1
  else:
    for i in range(1,n):
      if flag == False and h[i] == 0: continue
      if flag == True and h[i] == 0: break
      flag = True
      h[i] -= 1
    ans += 1
      
print(ans)      