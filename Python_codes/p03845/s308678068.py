import copy
n = int(input())
t = list(map(int,input().split()))
m = int(input())
p = [list(map(int,input().split())) for l in range(m)]
for pp in p:
	tmp = copy.copy(t)
	tmp[pp[0]-1] = pp[1]
	print(sum(tmp))

	
    