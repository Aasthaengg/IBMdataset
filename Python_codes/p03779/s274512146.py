def solve():
    X = int(input())
    cnt = 0
    sm = 0
    while sm < X:
        sm += cnt + 1
        cnt += 1

    print(cnt)

if __name__ == '__main__':
    solve()