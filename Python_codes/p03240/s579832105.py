
def solve():
    for i in range(N):
        if xyh[i][2] > 0:
            x,y,h = xyh[i][0], xyh[i][1], xyh[i][2]
            break

    for i in range(101):
        for j in range(101):
            H = h + abs(x-i) + abs(y-j)
            a = 0
            for k in range(N):
                if xyh[k][2] == max(H-abs(xyh[k][0]-i) - abs(xyh[k][1]-j), 0):
                    continue
                else:
                    a = 1
                    break
            if a == 0:
                print(i,j,H, sep=" ")
                break
        else:
            continue


if __name__ == "__main__":
    N = int(input())
    xyh = [list(map(int, input().split())) for _ in range(N)]
    solve()
