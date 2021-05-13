r, c = map(int,input().split())

Tbl = [list(map(int,input().split())) for i in range(r)]

for j in range(r):
	rS = sum(Tbl[j])
	Tbl[j].append(rS)

cS =[]
for k in range(c+1):
	s = 0
	for l in range(r):
		s += Tbl[l][k]
	cS.append(s)

Tbl.append(cS)

Tblp = [print(" ".join(map(str, Tbl[m]))) for m in range(r+1)]