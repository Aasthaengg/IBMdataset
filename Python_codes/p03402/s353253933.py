a,b = map(int,input().split())
print(100,100)

for i in range(50):
    if i%2 == 1:
        print("#"*(100))
    else:
        res = []
        for j in range(100):
            if j%2 == 1:
                res.append("#")
            elif a > 1:
                res.append(".")
                a -= 1
            else:
                res.append("#")
        print("".join(res))

for i in range(50):
    if i%2 == 0:
        print("."*(100))
    else:
        res = []
        for j in range(100):
            if j%2 == 1:
                res.append(".")
            elif b > 1:
                res.append("#")
                b -= 1
            else:
                res.append(".")
        print("".join(res))