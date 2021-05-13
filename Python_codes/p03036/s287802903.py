a,b,c = tuple(map(int,input().split()))
for i in range(10):
    c = a * c - b
    print(c)