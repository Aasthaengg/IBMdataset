import itertools
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

pcnt = 0
qcnt = 0
cnt=1

for l in itertools.permutations(range(1,n+1)):
    if p == l:
        pcnt = cnt
        break
    else:
        cnt += 1

cnt=1
for l in itertools.permutations(range(1,n+1)):
    if q == l:
        qcnt = cnt
        break
    else:
        cnt += 1
        
    #print(l)

print(abs(qcnt-pcnt))
