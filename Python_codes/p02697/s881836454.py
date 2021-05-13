## coding: UTF-8
N,M = map(int,input().split())

if(N % 2 == 1):
    pairs = []
    s = 2
    g = N
    for i in range(M):
        pairs.append([s, g])
        s += 1
        g -= 1
elif(N % 4 != 0):
    MAX = int(N/2) - 1
    half = int(MAX/2)
    pairs = []
    s = 1
    g = N
    for i in range(half):
        pairs.append([s, g])
        s += 1
        g -= 1
    g -= 1
    for i in range(half):
        pairs.append([s, g])
        s += 1
        g -= 1
else:
    odd_pairs = int(N/4)
    even_pairs = odd_pairs - 1
    pairs = []
    s = 1
    g = N
    for i in range(odd_pairs):
        pairs.append([s, g])
        s += 1
        g -= 1
    g -= 1
    for i in range(even_pairs):
        pairs.append([s, g])
        s += 1
        g -= 1







for i in range(M):
    print('{} {}'.format(pairs[i][0], pairs[i][1]))
#print(pairs)
