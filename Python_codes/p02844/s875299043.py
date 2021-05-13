N = int(input())
S = input()

lst = [0]*10

dic = {(i,j):set() for i in range(10) for j in range(10)}
a = set()
b = set()

for s_ in S:
  s = int(s_)
  for t in b:
    dic[t].add(s)
  for i in a:
    b.add((i,s))
  a.add(s)

rlt = 0
for c in dic:
  rlt += len(dic[c])
  
print(rlt)