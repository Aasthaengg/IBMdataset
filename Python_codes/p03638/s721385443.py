h, w = map(int, input().split())
n = int(input())
l = list(map(int, input().split()))
 
ans = []
for i in range(n):
  ans += [i+1]*l[i]

for i in range(h):
  temp = ans[i*w:(i+1)*w]
  if i%2 == 0:
    print(*temp)
  else:
    temp = reversed(temp)
    print(*temp)