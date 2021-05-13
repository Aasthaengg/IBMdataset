n, m, x = map(int, input().split())
lst = list(map(int, input().split()))
import bisect
z = bisect.bisect_left(lst, x)
#print(z)
print(min(len(lst[:z]), len(lst[z:])))