x,y = map(int, input().split())
for i in range(60,-1,-1):
    if x*(2**i) <= y:
        print(i+1)
        break