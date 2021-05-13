import itertools
n,m,r = map(int,input().split())
ri = [int(i) for i in input().split()]
#abc = [[int(i) for i in input().split()] for j in range(m)]

mat=[[10**18 for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
	mat[i][i]=0

for i in range(m):
	a,b,c=map(int,input().split())
	mat[a][b] = c
	mat[b][a] = c

for i in range(1,n+1):
	for x in range(1,n+1):
		for y in range(1,n+1):
			mat[x][y] = min(mat[x][y], mat[x][i] + mat[i][y])
            
            
permutations = list(itertools.permutations(range(1, r+1)))
#p = permutations.index(p)

#print(mat)
#exit()
ans = 10**18

for i in range(len(permutations)):
    tmp = 0
    for j in range(r-1):
        #print(permutations[i][j],permutations[i][j+1])
        tmp += mat[ri[permutations[i][j]-1]][ri[permutations[i][j+1]-1]]
    ans = min(ans,tmp)
    #print(permutations[i][0])
print(ans)