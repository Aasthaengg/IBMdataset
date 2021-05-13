N = int(input())
VG = []
for i in range(N//2):
  VG.append([i+1,(N//2)*2-i])
if N % 2 == 1:
  VG.append([N])
#print(VG)

E = []
for i in range(len(VG)-1):
  for v in VG[i]:
    for j in range(i+1,len(VG)):
      for u in VG[j]:
        E.append([v,u])
#print(E)

print(len(E))
for e in E:
  print(*e)