a,b = map(int,input().split())
for i in range(0,20):
    if a*(i-1) -(i-2)  < b <= a*i -(i-1):
        print(i)
        break
