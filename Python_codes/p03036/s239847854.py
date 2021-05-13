r,d,x = map(int, input().split())
i = 0
for i in range(1,11):
    x = r*x-d
    print(x)
    i+=1