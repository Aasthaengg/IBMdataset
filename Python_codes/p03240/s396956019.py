N = int(input())
info =[list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x: x[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        candidate_h = info[0][2] + abs(info[0][0] - cx) + abs(info[0][1] - cy)
        for i in range(1, N):
            x, y, h = info[i]
            if max(candidate_h - abs(x - cx) - abs(y - cy), 0) != h:
                break
        else:
            print("{} {} {}".format(cx, cy, candidate_h))
            exit()
