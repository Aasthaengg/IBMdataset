h,w = map(int,input().split())
c = [0]*h
for i in range(h):
    c[i] = list(map(int,input().split()))

L = []
for i in range(h):
    for j in range(w):
        if c[i][j]%2 == 1:
            
            if j != w-1:
                c[i][j] -= 1
                c[i][j+1] += 1
                L.append([str(i+1),str(j+1),str(i+1),str(j+2)])
                
            else:
                if i != h-1:
                    c[i][j] -=1
                    c[i+1][j] += 1
                    L.append([str(i+1),str(j+1),str(i+2),str(j+1)])
                    
print(len(L))
for x in L:
    print(" ".join(x))