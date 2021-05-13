x,y,z = map(int,input().split())

ans = 0

s = []

while True:
    if x%2 == 0 and y%2 == 0 and z%2 == 0:
        ans += 1
        if [x,y,z] in s:
            print(-1)
            break
        else:
            s.append([x,y,z])
    else:
        print(ans)
        break
    
    x,y,z = y//2+z//2,x//2+z//2,x//2+y//2