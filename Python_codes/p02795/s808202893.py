h = int(input())
w = int(input())
n = int(input())
 
ans = 0
sum = 0
 
while(sum < n):
  if h >= w :
    sum += h
    ans += 1
    w -= 1
  else :
    sum += w
    ans += 1
    h -= 1
print(ans)