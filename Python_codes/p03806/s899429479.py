
N,Ma,Mb = map(int,input().split())

lis = [[float("inf")] * 401 for i in range(401)]
lis[0][0] = 0

for x in range(N):

    a,b,c = map(int,input().split())

    olis = []
    for i in lis:
        new = []
        for j in i:
            new.append(j)
        olis.append(new)

    for i in range(401):

        for j in range(401):

            if olis[i][j] != float("inf"):

                if i + a < 400 and j + b < 400:

                    lis[i+a][j+b] = min( olis[i][j] + c , lis[i+a][j+b] )

ans = float("inf")

for i in range(400):

    i += 1

    for j in range(400):

        j += 1

        if i * Mb == j * Ma:

            ans = min(ans , lis[i][j])

if ans == float("inf"):
    print (-1)
else:
    print (ans)
