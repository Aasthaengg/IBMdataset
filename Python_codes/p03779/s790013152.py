import collections
target = int(raw_input())
t = 0
while(target):
	target -= min(target, t + 1)
	t +=1
print t