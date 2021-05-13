import sys
input = sys.stdin.readline

n, q = map(int, input().split())
events = []
for _ in range(n):
    s, t, x = map(int, input().split())
    events.append((s-x-0.5, 's', x)) # start construction
    events.append((t-x-0.5, 'e', x)) # end construction

for i in range(q):
    d = int(input())
    events.append((d, 'q', i)) # query
    
events = sorted(events)
is_stop = False
stops = set()
min_stop = float('inf')
ans = [-1]*q
for t, e, x in events: # time, event, distance/index
    if e == 's':
        stops.add(x)
        if x < min_stop:
            min_stop = x
            is_stop = True
    elif e == 'e':
        stops.remove(x)
        if min_stop == x:
            is_stop = False
    elif len(stops) > 0:
        if not is_stop:
             min_stop = min(stops)
             is_stop = True
        ans[x] = min_stop
         
for a in ans:
    print(a)