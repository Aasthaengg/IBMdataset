n = int(input())
a = [0] + list(map(int, input().split()))
ball = [0] * (n+1)

for i in range(n,0,-1):
  s = sum(ball[i: :i])
  if s % 2 == a[i]:
    ball[i] = 0
  else:
    ball[i] = 1

ans = []
for i in range(1,n+1):
  if ball[i] == 1:
    ans += [str(i)]
    
if ans:
  print(len(ans))
  print(" ".join(ans))
else:
  print(0)
  
  


