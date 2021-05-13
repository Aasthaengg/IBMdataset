N = int(input())
As = list(map(int, input().split()))

cnt = 0
m = 0
for a in As:
  if a < 0:
    cnt += 1
    
if cnt % 2 == 0:
  print(sum(map(abs, As)))
else:
  print(sum(map(abs, As))-2*min(map(abs, As)))