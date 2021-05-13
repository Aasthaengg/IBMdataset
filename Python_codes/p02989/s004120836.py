n = int(input())
d = list(map(int,input().split()))
sorted_d = sorted(d)

halfLength = int(len(sorted_d) / 2)

if sorted_d[halfLength-1] ==  sorted_d[halfLength]:
	print(0)
else:
	print(sorted_d[halfLength] - sorted_d[halfLength-1])