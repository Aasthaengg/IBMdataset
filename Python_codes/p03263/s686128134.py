def solve():
    h, w = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if l[i][j] % 2:
                if j == w-1:
                    if i == h-1:
                        continue
                    else:
                        l[i+1][j] += 1
                        ans.append('{} {} {} {}'.format(i+1, j+1, i+2, j+1))
                else:
                    l[i][j+1] += 1
                    ans.append('{} {} {} {}'.format(i+1, j+1, i+1, j+2))
    print(len(ans))
    for i in ans:
        print(i)


if __name__ == '__main__':
    solve()
