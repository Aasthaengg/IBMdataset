kazu = int(raw_input())
arr = []
s = raw_input().rstrip().split(" ")
for i in xrange(kazu):
	arr.append(int(s[i]))
print min(arr),max(arr),sum(arr)