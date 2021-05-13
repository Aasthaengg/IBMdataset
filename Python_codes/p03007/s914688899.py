n = int(input())
a = [int(i) for i in input().split()]
pos = [i for i in a if i >= 0]
neg = [i for i in a if i < 0]
cntp = len(pos)
cntn = len(neg)
lst = []

if pos and neg:
    for i in range(1,cntp):
        lst.append((neg[0],pos[i]))
        neg[0] -= pos[i]
    for i in range(1,cntn):
        lst.append((pos[0],neg[i]))
        pos[0] -= neg[i]
    lst.append((pos[0],neg[0]))
    maxv = pos[0]-neg[0]
elif pos:
    pos.sort()
    for i in range(1,cntp-1):
        lst.append((pos[0],pos[i]))
        pos[0] -= pos[i]
    lst.append((pos[cntp-1],pos[0]))
    maxv = pos[cntp-1]-pos[0]
else:
    neg.sort(reverse=True)
    for i in range(1,cntn):
        lst.append((neg[0],neg[i]))
        neg[0] -= neg[i]
    maxv = neg[0]
print(maxv)
for x,y in lst: print(x,y)