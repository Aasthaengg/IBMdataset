ny = input().split(" ")
n = int(ny[0])
y = int(ny[1])

for a in range(n+1):
    for b in range(n -a + 1):
        c = n - a -b
        if a*10000+b*5000+c*1000 == y:
            print("{} {} {}".format(a, b, c))
            exit()
print("-1 -1 -1")