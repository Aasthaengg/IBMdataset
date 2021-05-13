h, w = map(int, input().split())
A = [list(map(int, input().split())) for _  in range(h)]
tates = []
moves = []
for j, line in enumerate(A):
    odd = 0
    for i, a in enumerate(line[:w-1]):
        if a%2==1:
            odd ^= 1
        if odd:
            moves.append((j+1, i+1, j+1, i+2))
    tates.append(odd^(line[-1]%2))

odd = 0
for i, a in enumerate(tates[:h-1]):
    if a:
        odd ^= 1
    if odd:
        moves.append((i+1, w, i+2, w))

print(len(moves))
for m in moves:
    print(*m)

