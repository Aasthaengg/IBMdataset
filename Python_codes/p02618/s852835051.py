import copy
D = int(input())
c = list(map(int,input().split()))
s = [ [0 for j in range(26)] for i in range(D)]
for i in range(D):
    tmp = list(map(int,input().split()))
    for j in range(26):
        s[i][j] = tmp[j]
t = []
v = [0] * D
last = [ [0 for j in range(26)] for i in range(D)]
sum = 0
for i in range(D):
    max = -10000
    tmp_last = copy.deepcopy(last)
    for j in range(26):
        tmp_sum = sum
        if j != 0:
            tmp_last[i][j-1] = last[i][j-1]
        tmp_sum += s[i][j]
        tmp_last[i][j] = i+1
        for k in range(26):
            tmp_sum -= c[k] * ( (i+1) - tmp_last[i][j] )
        if tmp_sum > max:
            max_j = j
            max = tmp_sum
            last[i][j] = i+1
    sum = max
    t.append(max_j+1)


for i in range(D):
    print(t[i])