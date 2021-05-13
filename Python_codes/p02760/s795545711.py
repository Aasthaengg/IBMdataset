X = 3
bingo = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
def checkbingo(a):
    for i,j,k in bingo:
        if a[i] + a[j] + a[k] == 0:
            return True 
    return False
    
    

a = []
for i in range(X):
    a += list(map(int,input().split()))
    
N = int(input())
for j in range(N):
    b = int(input())
    if b in a:
        a[a.index(b)] = 0
if checkbingo(a):
    print('Yes')
else:
    print('No')
