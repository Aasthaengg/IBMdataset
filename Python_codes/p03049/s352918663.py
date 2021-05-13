n = int(input())
hB = set()
tA = set()
cAB = 0
for i in range(n):
    s = input()
    cAB += s.count('AB')
    if s[0] == 'B': hB.add(i)
    if s[-1] == 'A': tA.add(i)
if len(hB&tA)>0:
    if len(hB)-len(hB&tA)>0 or len(tA)-len(hB&tA)>0:
        print(cAB+min(len(hB),len(tA)))
    else:
        print(cAB+min(len(hB),len(tA))-1)
else:
    print(cAB+min(len(hB),len(tA)))