n = int(input())
sp = []
for i in range(n):
  s_, p_,  = input().split()
  sp.append([s_, int(p_)])

sp1 = sp
sp2 = sorted(sp, key=lambda x:(x[0], -x[1]))

for i in range(n):
  print(sp1.index(sp2[i])+1)