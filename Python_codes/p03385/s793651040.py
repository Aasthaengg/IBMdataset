import collections
counter = collections.Counter()

for i in input():
  	counter[i] += 1

if len([i for i in counter.values() if i >= 1]) == 3:
	print("Yes")
else:
    print("No")