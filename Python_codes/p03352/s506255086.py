x = int(input())

expo = [0]*(x+1)
expo[1] = 1

for i in range(2,x+1):
    v = i*i
    while v <= x:
        expo[v] = 1
        v *= i
        
for i in range(x,-1,-1):
    if expo[i]:
        print(i)
        exit()