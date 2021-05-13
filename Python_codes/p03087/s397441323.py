from sys import stdin

n,q = map(int,stdin.readline().split())
s = input()
lr = [list(map(int,stdin.readline().split())) for i in [0]*q]

posac = []
for i in range(1,n):
    if s[i-1]+s[i]=="AC":
        posac.append(i)
posac.append(n+1)

idx = 0
loc = 0
numac = [0 for i in [0]*n]
for i in range(n):
    if posac[idx]==i:
        loc += 1
        idx += 1
    numac[i] = loc
numac.append(loc)

#print(numac)
for i in lr:
    l,r = i[0]-1,i[1]-1
    print(numac[r]-numac[l])