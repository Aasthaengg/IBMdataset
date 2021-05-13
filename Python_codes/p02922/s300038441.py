a,b = map(int,input().split())
for i in range(20):
    if b == 1:
        print(0)
        break
    elif a +(a-1)*i >=b:
        print(i+1)
        break