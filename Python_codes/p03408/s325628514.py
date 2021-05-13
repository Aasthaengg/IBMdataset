import collections

N = int(input())
nlist = []
for i in range(N):
    nlist.append(input())

M = int(input())
mlist = []
for i in range(M):
    mlist.append(input())

for i in mlist:
    if i in nlist:
        nlist.remove(i)

nlist = collections.Counter(nlist).most_common()

if nlist==[]:
    print(0)
    exit()

print(nlist[0][1])