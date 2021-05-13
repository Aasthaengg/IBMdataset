a,b = map(int, input().split())
for i in range(1,1011):
    
    if int(i*0.08) == a and int(i*0.1) == b:
        print(i)
        break
    elif a < int(i*0.08) and b < int(i*0.1):
        print(-1)
        break