x,y = map(int,input().split())
count = 0

ans = x
while ans <= y:
  ans = ans * 2
  count = count + 1

print(count)