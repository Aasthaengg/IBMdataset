import functools
import  sys

sys.setrecursionlimit(10**6)
@functools.lru_cache()
def ryuca(l):
	if l == 0:
		return 2
	elif l == 1:
		return 1
	else:
		 return ryuca(l-1) + ryuca(l-2)
print(ryuca(int(input())))
