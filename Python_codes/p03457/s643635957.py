N = int(input())
t = 0
x = 0
y = 0
for i in range(N):
    t1,x1,y1 = map(int,input().split())
    if abs(x1-x) + abs(y1-y) > t1-t or (abs(x1-x) + abs(y1-y) - (t1-t)) % 2 != 0:
        print('No')
        exit(0)
    t,x,y = t1,x1,y1
print('Yes')