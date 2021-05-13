r,D,x = (int(a) for a in input().split())
count = 0
while count <= 9 :
    x = r * x - D
    print(x)
    count += 1
