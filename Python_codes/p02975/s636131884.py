# coding: utf-8
N = int(input())
A = list(map(int, input().split()))
# A.sort()
d = {}
for i in range(N):
    a = A[i]
    if a not in d.keys():
        d[a] = 1
    else:
        d[a] += 1
flag = True
if len(d.keys()) == 1:
    if list(d.keys())[0] == 0:
        flag = True
    else:
        flag = False
elif len(d.keys()) == 2:
    keys = list(sorted(list(d.keys())))
    if d[keys[0]] == N // 3:
        flag = True
    else:
        flag = False
elif len(d.keys()) == 3:
    keys = list(d.keys())
    if keys[0] ^ keys[1] ^ keys[2] == 0:
        if d[keys[0]] == d[keys[1]] == d[keys[2]]:
            flag = True
        else:
            flag = False
    else:
        flag = False
else:
    flag = False
print("Yes" if flag else "No")