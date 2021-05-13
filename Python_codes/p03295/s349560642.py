N, M = list(map(int,input().split()))
a = []
for i in range(M):
    a.append(list(map(int,input().split())))
a = sorted(a, key=lambda x: x[1])
bridges = []

for i in range(M): 
    flag = 1
    for bridge in bridges:
        if a[i][0] <= bridge and bridge < a[i][1]:
            flag = 0
            break 
    if flag:	bridges.append(a[i][1] - 1)   
print(len(bridges))