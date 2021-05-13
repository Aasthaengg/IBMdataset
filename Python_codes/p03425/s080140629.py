import itertools
n = int(input())
counters = {"M":0,"A":0,"R":0,"C":0,"H":0}

for _ in range(n):
  s = input()[0]
  
  if s in "MARCH":
  	counters[s] += 1
res = 0
for i in list(itertools.combinations(["M","A","R","C","H"],3)):
  res += counters[i[0]] * counters[i[1]] * counters[i[2]]

print(res)