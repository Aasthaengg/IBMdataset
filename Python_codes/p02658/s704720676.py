n = input()
a = list(map(int,input().split()))
ans = 1
t = False

for i in a:
  if i == 0:
    ans = 0
    t = True

if t != True:
  for i in a:
    ans *=i
    if ans>10**18:
      ans = -1
      break
    
print(ans)