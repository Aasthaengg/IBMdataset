N,M = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(M)]
D = [[] for i in range(N)]
#print(lst)
submit =[0]*M
for i in range(M):
    D[lst[i][0]-1].append((lst[i][1],i))

#print(D)

for i,d in enumerate(D):
    #print(i,d)
    d.sort(key=lambda x: x[0])
    #print(d)
    for k,(y,j) in enumerate(d):
        #print(i,k,y,j)
        submit[j] = str(i+1).zfill(6)+str(k+1).zfill(6)

print(*submit,sep = '\n')