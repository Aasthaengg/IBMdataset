x,y = map(int,input().split())
ans = -1
i = 1

while True:
    a = (x*i) % y
    if a != 0:
        ans = x*i
        break
    else:
        ans = -1
        break

print(ans)