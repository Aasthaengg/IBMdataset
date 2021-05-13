N,Y=map(int,input().split())
answer=-1,-1,-1
for x in range(N+1):
    for y in range(N-x+1):
        z=N-x-y#多分起こりうる１０００円札の数
        if 0<=z<=2000 and 10000*x+5000*y+1000*z==Y:
            #左：お札は正の数
            #左：起こりうる１０００円札の数のときにY円になるかどうか
            answer=x,y,z
            break
    else:
        continue
    break
print(*answer)