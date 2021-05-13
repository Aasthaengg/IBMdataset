a,b = map(int,input().split())
if (a + b) % 2 == 1: 
    print('IMPOSSIBLE')
    exit()
print((a+b) // 2)