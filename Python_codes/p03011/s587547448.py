import itertools
p,q,r = map(int,input().split())
time = []
time.append(p)
time.append(q)
time.append(r)
time_min = float('inf')
for item in itertools.combinations(time,2):
    time_min = min(sum(item), time_min)
print(time_min)