N = int(input())
lis = [(input() + " " + str(i+1)).split() for i in range(N)]

lis = [k for k in lis]

lis.sort(key=lambda k: int(k[1]), reverse=True)
lis.sort(key=lambda k: k[0])


for j in lis:
    print(j[2])
