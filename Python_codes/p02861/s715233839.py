import math
def dis(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**(1/2))

N = int(input())
cord = []
tem = 0

for i in range(N):
    cord.append(list(map(int,input().split())))

for i in range(N):
    x1,y1 = cord[i]
    for j in range(0,i):
        x2,y2 = cord[j]
        tem += dis(x1,y1,x2,y2)    
    for j in range(i+1,N):
        x2,y2 = cord[j]
        tem += dis(x1,y1,x2,y2)

print(tem*math.factorial(N-1)/math.factorial(N))