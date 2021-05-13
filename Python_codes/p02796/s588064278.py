from operator import itemgetter

N = int(input())
l = []
for i in range(N):
  a, b = map(int, input().split())
  s = [a-b, a+b]
  l.append(s)

l.sort(key = itemgetter(1))
cnt = 0
s = - 10 ** 10
for i in range(N):
  if l[i][0] >= s:
    s = l[i][1]
  else:
    cnt += 1
print(N-cnt)