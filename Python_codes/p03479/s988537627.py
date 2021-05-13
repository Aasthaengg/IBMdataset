x,y = map(int,input().split())
count = 1
ans = x

for i in range(10**19):
  ans = ans*2
  if ans <= y:
    count += 1
  else:
    break
    
print(count)