n = int(input())
vert = [[0,0]+list(map(int,range(1,n+1)))]
parents = [0]
now = 0
time = 0
for i in range(n):
    ukv = list(map(int,input().split()))
    vert.append([0,0]+ukv[2:])
while(parents):
    for i in range(2,len(vert[now])):
        if vert[vert[now][i]][0] == 0:
            parents.append(now)
            now = vert[now][i]
            time += 1
            vert[now][0] = time
            break
    else:
        if now != 0:
            time += 1
        vert[now][1] = time
        now = parents.pop()
for i in range(1,n+1):
    print(i,*vert[i][0:2])
