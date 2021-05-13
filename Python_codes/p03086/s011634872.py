S = input()
 
ACGT = ['A', 'C', 'G', 'T']
cntList = []
cnt = 0
cntList.append(cnt)
for s in S:
    if s in ACGT:
        cnt += 1
        cntList.append(cnt)
    else:
        cnt = 0
print(max(cntList))