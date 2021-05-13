N,M = map(int,input().split())
#P = [list(map(int,input().split())) for i in range(M)]
D = [[] for i in range(N)]
#print(P.sort())
for i in range(M):
    p,y = map(int,input().split())
    D[p-1].append((y,i))
    

#D = [[(32,0),(12,2)],[(63,1)]]
#print(D)
submit = [0]*M
for i,d in enumerate(D):
    #print(d)
    d.sort()
    #print(i,d)
    for k, (y,j) in enumerate(d):
        #print(k,y,j)
        submit[j] = str(i+1).zfill(6)+str(k+1).zfill(6)
        
#print(submit)
print(*submit,sep = '\n')