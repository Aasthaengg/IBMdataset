def is_fin(x,y):
    if abs(x-y)==1:
        return False
    return True
n,a,b = map(int,input().split())
turn = 0
while is_fin(a,b):
    if turn%2==0:
        a += 1
    else:
        b -= 1
    turn += 1
print('Alice' if turn%2==1 else 'Borys')