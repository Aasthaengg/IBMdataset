import queue
n = int(input())
h = list(map(int, input().split()))

q = queue.Queue()
ans = 0
def dec(ary):
  global q, ans
  m = min(ary)
  ans += m
  tmp = []
  for i in range(len(ary)):
    t = ary[i] - m
    if t > 0:
      tmp.append(t)
    else:
      if len(tmp) > 0:
        q.put(tmp)
      tmp = []
  if len(tmp) > 0:
    q.put(tmp)
tmp = []
for i in range(n):
  if h[i] > 0:
    tmp.append(h[i])
  else:
    if len(tmp) > 0:
      #print(tmp)
      q.put(tmp)
    tmp = []

if len(tmp) > 0:
  q.put(tmp)

while q.empty() == False:
  dec(q.get())
print(ans)