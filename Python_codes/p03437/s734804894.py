x,y = map(int,input().split())
if x % y == 0:
    ans = -1
else:
    i = 1
    while i < y:
        if (i*x)%y != 0:
            ans = i*x
            break
print(ans)