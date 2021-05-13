from collections import deque
h,w = map(int,input().split())
mapa=[]
mapa.append(''.join(['#' for _ in range(w+2)]))
dotn = 0
for i in range(h):
    temp = input()
    dotn+=temp.count('.')
    mapa.append('#'+temp+'#')
mapa.append(''.join(['#' for _ in range(w+2)]))
passed = [[False for _ in range(w+2)] for _ in range(h+2)]

def dircheck(cy,cx):
    if mapa[cy][cx]=='.' and not passed[cy][cx]:
        passed[cy][cx]=True
        return True
    else:
        return False    

q=deque()
q.append((1,1))
step=0
goaled=False
while True:
    newq=deque()
    while len(q)!=0:
        (y,x) = q.pop()
        if (y,x)==(h,w):
            goaled=True
            break
        else:
            for dy,dx in zip((y-1,y+1,y,y),(x,x,x-1,x+1)):
                if dircheck(dy,dx):newq.append((dy,dx))
    q = newq
    step+=1
    if goaled:
        print(dotn-step)        
        break
    if len(newq)==0:
        print(-1)
        break