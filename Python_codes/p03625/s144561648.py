from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
kouho = set([])
kouho2 = set([])
for i in c.most_common():
	if i[1] >= 2:
		kouho.add(i[0])
	if i[1] >= 4:
		kouho2.add(i[0])
kouholist = list(kouho)
kouholist2 = list(kouho2)
kouholist = kouholist + kouholist2
kouholist = sorted(kouholist)[::-1]
if len(kouholist) >= 2:
	print(kouholist[0]*kouholist[1])
else:
	print(0)