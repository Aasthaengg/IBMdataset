import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = []


for i in range(q):
    bci = list(map(int, input().split()))
    bc.append(bci)

cc = collections.Counter(a)
li = cc.most_common()
su = sum(a)

for i in range(q):
    b, c = bc[i]
    if cc[b]:
        num = (c-b)*cc[b]
    else:
        num = 0
    su += num
    print(su)
    if cc[c]:
        cc[c] += cc[b]
    else:
        cc[c] = cc[b]
    cc[b] = 0