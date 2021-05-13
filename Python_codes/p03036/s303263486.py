c = [int(i) for i in input().split() if i.isdigit()] 
for i in range(1,11):
    c[2] = (c[0] * c[2]) - c[1]
    print(c[2])