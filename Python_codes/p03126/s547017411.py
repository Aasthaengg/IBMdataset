import collections
n, m = map(int, raw_input().split(' '))
cc = collections.Counter()
for _ in range(n):
	for a in map(int, raw_input().split(' '))[1:]: cc[a] += 1
count = 0
for k in cc:
  	if cc[k] == n: count +=1
print count