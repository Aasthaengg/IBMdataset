x,y = map(int, input().split())

ans = 0
i = 1
while True:
    t = x*i
    if t > y:
        break
    
    ans += 1
    i = i*2
    

print(ans)