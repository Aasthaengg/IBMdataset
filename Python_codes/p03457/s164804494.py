N = int (input ())
t2 = 0
x2 = 0
y2 = 0
ans = 'Yes'
for i in range (N):
    t,x,y = map(int, input().split())
    if abs(x+y-x2-y2) <= t-t2:
        if ((abs(x2+y2-x-y))-(t-t2)) % 2 == 1:
            ans = 'No'
            break
    else:
        ans = 'No'
        break
    t2 = t
    x2 = x
    y2 = y
print (ans)