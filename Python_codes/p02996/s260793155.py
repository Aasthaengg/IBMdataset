from operator import itemgetter
N=int(input())
ab=[tuple(map(int,input().split())) for _ in range(N)]
ab=sorted(ab, key=itemgetter(1))
#print(ab)

c=0
for v in ab:
    if c+v[0]<=v[1]:
        c+=v[0]
    else:
        print('No')
        break
else:
    print('Yes')