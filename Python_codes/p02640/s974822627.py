x,y = map(int, input().split())
feet = 0
for i in range(x+1):
    feet = i*2+(x-i)*4
    if feet == y:
        print("Yes")
        break
else:
    print("No")