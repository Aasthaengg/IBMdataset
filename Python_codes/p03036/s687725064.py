a,b,c = tuple(map(int,input().split()))
for i in range(1,11):
    c = a * c - b
    print(c)