n, a, b, c = map(int, input().split())
bamboo = [0]*n
for i in range(n):
  bamboo[i] = int(input())

answer = 10**10
for i in range(4**n):
  key = [0, 0, 0, 0]
  sub = [0, 0, 0]
  for j in range(n):
    k = 0
    if (i >> (2*j))&1:
      k += 1
    if (i >> (2*j+1))&1:
      k += 2
    key[k] += 1
    if k != 3:
      sub[k] += bamboo[j]
  if not all(sub):
    continue
  ans = (sum(key[:3])-3)*10+abs(sub[0]-a)+abs(sub[1]-b)+abs(sub[2]-c)
  if ans < answer:
    answer = ans
print(answer) 