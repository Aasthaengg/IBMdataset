a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
dist = abs(a-b)
speed = v-w
if speed<=0:
    print('NO')
    exit()
if dist<=speed*t:
    print('YES')
else:
    print('NO')


