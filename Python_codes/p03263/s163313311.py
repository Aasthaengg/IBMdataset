H, W = map(int, input().split())
state = False
moves = []
ans = []
for i in range(H):
    row = tuple(zip(range(W), map(int, input().split())))
    for j, a in reversed(row) if i & 1 else row:
        if a & 1:
            state = not state
            if not state:
                moves.append((i + 1, j + 1))
                for pair in zip(moves[:-1], moves[1:]):
                    ans.append(sum(pair, tuple()))
                moves = []
        if state:
            moves.append((i + 1, j + 1))
print(len(ans))
for a in ans:
    print(*a)