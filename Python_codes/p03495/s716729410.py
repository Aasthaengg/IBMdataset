n,k = map(int,input().split())
from collections import defaultdict
d = defaultdict(int)
num_list = list(map(int,input().split()))
for tmp in num_list:
	d[tmp] += 1
    
v_list = sorted(list(d.values()) ,reverse=True)

print(n - sum(v_list[:k]))
