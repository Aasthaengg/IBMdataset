
N = int(input())
lis = []

if N % 2 == 0:

    S = N+1

    for i in range(N):

        for j in range(i):

            if (i+1) + (j+1) == S:
                continue

            else:
                lis.append([i+1,j+1])

else:

    S = N

    for i in range(N-1):

        for j in range(i):

            if (i+1) + (j+1) == S:
                continue

            else:
                lis.append([i+1,j+1])

    for i in range(N-1):
        lis.append([i+1,N])

print (len(lis))

for i in lis:

    print (i[0],i[1])