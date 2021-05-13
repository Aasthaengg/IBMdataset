b,a = map(int,input().split())
lis = []
for i in range(50):
	g = []
	for m in range(100):
		g.append(".")
	lis.append(g)
for i in range(50):
	g = []
	for m in range(100):
		g.append("#")
	lis.append(g)
cou = 0
co = 0
for k in range(a-1):
	lis[cou][co] = "#"
	co += 2
	if co >= 100:
		co = 0
		cou += 2
cou = 51
co = 0
for h in range(b-1):
	lis[cou][co] = "."
	co += 2
	if co >= 100:
		co = 0
		cou += 2
print("100 100")
for m in range(100):
	print("".join(lis[m]))