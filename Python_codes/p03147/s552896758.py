n = int(input())
h = list(map(int, input().split()))

ans = 0
while sum(h) != 0:
  flag = False
  for i in range(n):
    if h[i] != 0: flag = True
    if flag == True and h[i] == 0: break
    elif flag == False and h[i] == 0: continue
    h[i] -= 1
  ans += 1
print(ans)