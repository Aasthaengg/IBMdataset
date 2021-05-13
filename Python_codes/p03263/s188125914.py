H, W = map(int, input().split())

query = []
for i in range(H):
    if i%2==0:
        lis = [(i, j) for i, j in enumerate(list(map(int, input().split())))]
    else:
        lis = [(i, j) for i, j in enumerate(list(map(int, input().split())))][::-1]
    query += lis

odd = 0
move = []
last = (0, 0)
for i, (w, q) in enumerate(query):
    if odd:
        move.append((last[0], last[1], i//W+1, w+1))
        if q%2==1:
            odd = 0
        else:
            last = (i//W+1, w+1)
    else:
        if q%2==1:
            odd = 1
            last = (i//W+1, w+1)

print(len(move))
for l in move:
    print(*l)