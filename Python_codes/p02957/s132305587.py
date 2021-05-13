a,b = map(int,input().split())
k = (a+b) // 2
if (a+b)%2 != 0:
    print('IMPOSSIBLE')
    exit()
print(k)