from copy import deepcopy
n = int(input())
v = list(map(int, input().split()))

d1 = [0]*(10**5+1)
d2 = [0]*(10**5+1)
for i in range(n):
    if i%2: d2[v[i]] += 1
    else: d1[v[i]] += 1
        
max_d1 = [0, 0]
max_d2 = [0, 0]
submax_d1 = [0, 0]
submax_d2 = [0, 0]
for i in range(10**5+1):
    if max_d1[1] < d1[i]:
        submax_d1 = deepcopy(max_d1)
        max_d1[0] = i
        max_d1[1] = d1[i]
    elif submax_d1[1] < d1[i]:
        submax_d1[0] = i
        submax_d1[1] = d1[i]
    if max_d2[1] < d2[i]:
        submax_d2 = deepcopy(max_d2)
        max_d2[0] = i
        max_d2[1] = d2[i]
    elif submax_d2[1] < d2[i]:
        submax_d2[0] = i
        submax_d2[1] = d2[i]
if max_d1[0] == max_d2[0]:
    if max_d1[1] + submax_d2[1] > max_d2[1]+submax_d1[1]:
        print(n-max_d1[1]-submax_d2[1])
    else:
        print(n-max_d2[1]-submax_d1[1])
else:
    print(n-max_d1[1]-max_d2[1])