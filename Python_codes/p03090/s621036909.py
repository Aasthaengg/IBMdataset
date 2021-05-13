N = int(input())
if N == 3:
    print(2)
    print(1,3)
    print(2,3)
    exit()

if N == 4:
    print(4)
    print(1,2)
    print(1,3)
    print(4,2)
    print(4,3)
    exit()

if N%2 == 1:
    n = int((N+1)/2)
    group = [[0] * 2 for i in range(n-1)]
    M = n*4 - 4
    edge = []
    for i in range(n-1):
        group[i][0] = i+1
        group[i][1] = N-i-1
    for i in range(n-1):
        if i == n-2:
            edge.append([group[i][0],N])
            edge.append([group[i][1],N])
            edge.append([N,group[0][0]])
            edge.append([N,group[0][1]])
            #edge.append([group[i][1],group[i+1][0]])
            #edge.append([group[i][1],group[i+1][1]])    
        else:
            edge.append([group[i][0],group[i+1][0]])
            edge.append([group[i][0],group[i+1][1]])
            edge.append([group[i][1],group[i+1][0]])
            edge.append([group[i][1],group[i+1][1]])

if N%2 == 0:
    n = int(N/2)
    group = [[0] * 2 for i in range(n)]
    M = n*4
    edge = []
    for i in range(n):
        group[i][0] = i+1
        group[i][1] = N-i
    for i in range(n):
        if i == n-1:
            edge.append([group[i][0],group[0][0]])
            edge.append([group[i][0],group[0][1]])
            edge.append([group[i][1],group[0][0]])
            edge.append([group[i][1],group[0][1]]) 
        else:
            edge.append([group[i][0],group[i+1][0]])
            edge.append([group[i][0],group[i+1][1]])
            edge.append([group[i][1],group[i+1][0]])
            edge.append([group[i][1],group[i+1][1]])

print(M)
#print(group)
for m in range(M):
    print(edge[m][0],edge[m][1])