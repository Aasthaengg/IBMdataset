import statistics
import math
abc = list(map(int,input().split()))
max = max(abc)
med = statistics.median(abc)
min = min(abc)
cop = (max-med)+(max-min)
if cop%2 == 0:
	print(cop//2)
else:
	print(math.ceil(cop/2)+1)