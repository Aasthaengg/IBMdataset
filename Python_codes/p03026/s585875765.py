#解説チラ見
n = int(input())
peer = [[] for _ in range(n)]
for _ in range(n-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  peer[a].append(b)
  peer[b].append(a)
now = [0]
scr = list(map(int,input().split()))
scr.sort()
scr.reverse()
ans = [0 for _ in range(n)]
ans[0] = scr[0]
pin = 1
while now:
  last = now
  now = []
  for x in last:
    for y in peer[x]:
      if ans[y] == 0:
        ans[y] = scr[pin]
        pin += 1
        now.append(y)
print(sum(scr[1:]))
print(' '.join(list(map(str,ans))))