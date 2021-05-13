# 2019/12/12

a,b,k=map(int,input().split())
turn=1

def eat(x,y):
    if x%2:
        x-=1
    x//=2
    y+=x
    return x,y

for i in range(k):
    if turn:
        a,b=eat(a,b)
    else:
        b,a=eat(b,a)
    turn=1-turn
print('{} {}'.format(a,b))