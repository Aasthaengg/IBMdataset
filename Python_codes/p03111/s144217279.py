from itertools import permutations
from copy import deepcopy
from collections import Counter

n,a,b,c = map(int,input().split())
take = []
for _ in range(n):
	take.append(int(input()))
tmp = deepcopy(take)
ans_list = []

sum_abc = 10 ** 5
for abc in permutations([a,b,c],3):
	take = deepcopy(tmp)
	ans = 0
	l = []
	l2 = []
	s = Counter(take)
	#print(s)
	for x in abc:
		res = []
		l2 = []
		take = []
		for i,num in s.items():
			for j in range(num):
				take.append(i)
		#take = list(s)
		for i in range(2**n):
			l = []
			for j in range(len(take)):
					if i & (1<<j):
						l.append(take[j])
			if len(l) == 0:
				continue
			res.append(10*(len(l)-1) + abs(sum(l) - x))
			l2.append(l)
		minimum = sum_abc
		for i in range(len(res)):
			if minimum > res[i]:
				minimum = res[i]
				s2 = l2[i]
		for i in range(len(s2)):
			s[s2[i]] -= 1
			if s[s2[i]] == 0:
				s.pop(s2[i])
		#s = s - s2
		ans += minimum
		#print(res,s,minimum)
	ans_list.append(ans)

print(min(ans_list))
