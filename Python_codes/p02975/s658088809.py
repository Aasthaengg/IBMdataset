N = int(input())
a = list(map(int,input().split()))
b = {}
flag = 0
ke = []
for i in range(N):
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] = 1

if 0 in b:
    if b[0] == N:
        flag = 1

if len(b) == 2:    
    for key in b:
        ke.append(key)  
    if 0 in b:
        if b[ke[1]] / b[0] == 2 or b[ke[0]] / b[0] == 2:
            flag = 1

if len(b) == 3:
    for key in b.keys():
        ke.append(key)

    if b[ke[0]] == b[ke[1]] and b[ke[1]] == b[ke[2]]:
        if ke[0] ^ ke[1] == ke[2] or ke[1] ^ ke[2] == ke[0] or ke[0] ^ ke[2] == ke[1]:
            flag = 1

if flag == 1:
    print('Yes')
else:
    print('No')


