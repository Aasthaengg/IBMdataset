import collections
h,t= {p: collections.deque(list(raw_input())) for p in 'abc'},'a'
while(h[t]): t  = h[t].popleft()
print t.upper()