# h, a = map(int, input().split())
from collections import OrderedDict
d = OrderedDict()
a = list(input().split())
b = list(map(int, input().split()))
for i in range(2):
	d[a[i]] = b[i]
d[input()] -= 1
print(*d.values())