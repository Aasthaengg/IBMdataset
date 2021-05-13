a,b,c = map(int,input().split())
x = a * c - b
for _ in range(10):
    print(x)
    x = a * x - b