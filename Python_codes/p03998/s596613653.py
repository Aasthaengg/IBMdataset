from collections import deque
aq = deque(input())
bq = deque(input())
cq = deque(input())
d={"a":aq,"b":bq,"c":cq}
p=aq.popleft()
while True:
  if len(d[p])==0:
    print(p.upper())
    exit()
  p=d[p].popleft()