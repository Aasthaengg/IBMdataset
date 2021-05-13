h,w = map(int,input().split())
l = [['']*(w+2)]
for i in range(h):
    l.append(['']+list(input())+[''])
l.append(['']*(w+2))
for i in range(1,h+1):
    for j in range(1,w+1):
        if l[i][j] == '#':
            flag = False
            for k in [(-1,0),(1,0),(0,-1),(0,1)]:
                if l[i + k[0]][j + k[1]] == '#':
                    flag = True
            if not flag:
                print('No')
                exit()
print('Yes')