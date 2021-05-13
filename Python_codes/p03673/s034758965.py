n = int(input())
List = list(map(int,input().split()))
direction = 1
ahead = []
post = []
for i in range(n):
  if direction == 1:
    post.append(List[i])
  else:
    ahead.append(List[i])
  direction *= -1
if direction == 1:
  ans = ahead[::-1]+post
else:
  ans = post[::-1]+ahead
print(*ans)
