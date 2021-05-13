n,m = map(int, input().split())
AL = []
for i in range(n):
 ALI = list(map(int, input().split()))
 AL.append(ALI)

BL = []
for i in range(m):
 BL.append(int(input()))

for i  in AL:
 Ci = 0
 for (j, ai) in enumerate(i):
  Ci += ai * BL[j]
 print(Ci)