r,d,x = map(int,input().split())
[print(int(r**i*(x+d/(1-r))-d/(1-r))) for i in range(1,11)]