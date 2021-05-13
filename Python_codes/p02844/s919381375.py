n=int(input())
s=input()

all=[]
for i in range(10):
	for j in range(10):
		for k in range(10):
			all.append(str(i) + str(j) + str(k))

output=0
for i in range(n):
	tmps=s[i]
	tmplist=[]
	
	for j,x in enumerate(all):
		if x[0] == tmps:
			if len(x)==1:
				tmplist.append(x)
				output += 1
			else:
				all[j] = x[1:]
	
	for tmp in tmplist:
		all.remove(tmp)

print(output)

