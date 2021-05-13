import copy
s = input()
x,y = map(int,input().split())

ver = []
hor = []
ini = 0
flag = 'h1'
tmp = 0

for i in range(len(s)):
    if s[i] == 'T':
        if flag == 'h':
            if tmp > 0:
                hor.append(tmp)
            tmp = 0
            flag = 'v'
        elif flag == 'v':
            if tmp > 0:
                ver.append(tmp)
            flag = 'h'
            tmp = 0
        elif flag == 'h1':
            if tmp > 0:
                ini = tmp
            flag = 'v'
            tmp = 0
    else:
        tmp += 1

if tmp > 0:
    if flag == 'h1':
        ini = tmp
    elif flag == 'h':
        hor.append(tmp)
    elif flag == 'v':
        ver.append(tmp)

num = 8000
        
ver_li = [[0 for i in range(2)] for j in range(num*2+1)]
hor_li = [[0 for i in range(2)] for j in range(num*2+1)]

hor_li[num+ini][0] = 1
#print(sum(hor))
#exit()

for i in range(len(hor)):
    #c_hor = copy.deepcopy(hor_li)
    for j in range(num*2+1):
        if hor_li[j][0] == 1:
            #print(j,hor[i],i)
            hor_li[j][1] = 0
            hor_li[j+hor[i]][1] = 1
            hor_li[j-hor[i]][1] = 1
    for j in range(num*2+1):
        hor_li[j][0] = hor_li[j][1]

ver_li[num][0] = 1
for i in range(len(ver)):
    #c_ver = copy.deepcopy(ver_li)
    for j in range(num*2+1):
        if ver_li[j][0] == 1:
            ver_li[j][1] = 0
            #print(hor[i])
            ver_li[j+ver[i]][1] = 1
            ver_li[j-ver[i]][1] = 1
    for j in range(num*2+1):
        ver_li[j][0] = ver_li[j][1]
    
if hor_li[num+x][0] == 1 and ver_li[num+y][0] == 1:
    print('Yes')
else:
    print('No')