x,y,z = map(int,(input().split()))
a=z
for b in range(10):
    a = x*a-y
    print(a)
