from itertools import product

N = int(input())

li = [[] for i in range(N)]
A = [0]*N
for i in range(N):
    a = int(input())
    A[i]=a
    li[i]=[list(map(int,input().split())) for i in range(a)]

counter = 0
for humen in product([0,1],repeat=N):
    flag = True
    for i in range(N):
        if humen[i]==1:
            for s in range(A[i]):
                if not li[i][s][1]==humen[li[i][s][0]-1]:
                    flag=False
                    break
        
                
    if flag :
        counter = max(counter,humen.count(1))


print(counter)