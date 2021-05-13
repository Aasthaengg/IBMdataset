N,M = map(int,input().split())

glaf = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a=a-1
    b=b-1
    glaf[a].append(b)
    glaf[b].append(a)
    
for i in glaf:
    cnt =0
    for j in i:
        cnt+=1
    
    print(cnt)