N,x = map(int,input().split())
C = 0
r = 1000000
for i in range(N):
    l = int(input())
    x -=l
    C +=1
    r = min(l,r)

while x>=r:
    x = x - r
    C +=1
    
print(C)    