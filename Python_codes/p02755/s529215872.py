a,b = map(int,input().split())

for i in range(1,10000):
    aa = ( i * 8 ) // 100
    bb = ( i * 10 ) // 100
    if aa == a and bb == b:
        print(i)
        exit()
print("-1")