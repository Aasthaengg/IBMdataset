N,M = list(map(int,input().split()))
PY = [list(map(int,input().split())) + [i] for i in range(M)]

from operator import itemgetter
PY= sorted(PY,key=itemgetter(1),reverse = False)
PY = sorted(PY,key=itemgetter(0),reverse = False)

B= []
pre = 0
city = 0
for i in range(M):
    if pre != PY[i][0]:
        pre =  PY[i][0]
        city = 1
        B.append([str(pre).rjust(6, '0') + str(city).rjust(6, '0') ,PY[i][2]])
    else:
        city += 1
        B.append([str(pre).rjust(6, '0') + str(city).rjust(6, '0') ,PY[i][2]])

B= sorted(B,key=itemgetter(1),reverse = False)        
for i in range(M):
    print(B[i][0])