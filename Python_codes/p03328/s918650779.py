a,b = map(int,input().split())
x = 1
y = 3
for i in range(10**5):
    if x-a == y-b:
        print(x-a)
        break
    else:
        x += i+2
        y += i+3