def solve():

    N = int(input())

    prots = []

    for _ in range(N):
        x, y, h = map(int, input().split())
        prots.append([h, x, y])

    # 高さ０をモデルケースにしない
    prots.sort(reverse=True)

    for centerx in range(101):
        for centery in range(101):
            h, x, y = prots[0]
            # 仮置
            H = h+abs(centerx - x) + abs(centery - y)
            flag = True
            for i in range(N):
                h, x, y = prots[i]
                if h != max(0, H-abs(centerx - x) - abs(centery - y)):
                    flag = False
                    break
            if flag:
                print(centerx, centery, H)
                exit()


if __name__ == "__main__":
    solve()
