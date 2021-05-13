#%%
t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

x = (a1-b1) * t1
y = x + (a2-b2) * t2
#print(x, y)

def p(x, y):
    if x%y == 0:
        return abs(x//y)
    else:
        return abs(x//y) + 1

if y == 0:
    ans = 'infinity'
else:
    if x%y != 0:
        if x < 0 and y > 0 :
            ans = (abs(x//y) + 1) * 2 - 3
        elif x > 0 and y < 0 :
            ans = (abs(x//y) + 1) * 2 - 3
        else:
            ans = 0
    else:
        if x < 0 and y > 0 :
            ans = (abs(x//y) + 1) * 2 - 2
        elif x > 0 and y < 0 :
            ans = (abs(x//y) + 1) * 2 - 2
        else:
            ans = 0


print(ans)