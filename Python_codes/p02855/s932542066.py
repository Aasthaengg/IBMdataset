H, W, K = map(int, input().split(" "))
cake = [input() for _ in range(H)]

is_strawberry = []
for i in cake:
    is_strawberry.append(('#' in i))

cut = [[0 for _ in range(W)] for _ in range(H)]
num = 1
for h, c in enumerate(cake):
    if is_strawberry[h]:
        st_count = sum([s == '#' for s in c])
        for w in range(W):
            if cake[h][w] == '.' or st_count == 0:
                cut[h][w] = num
            else:
                cut[h][w] = num
                st_count -= 1
                if st_count > 0:
                    num += 1
        num += 1

ind = is_strawberry.index(True)
for h in range(H):
    if not is_strawberry[h]:
        for w in range(W):
            cut[h][w] = cut[ind][w]
    else:
        ind = h

for c in cut:
    print(' '.join([str(s) for s in c]))