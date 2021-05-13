from sys import stdin
input = stdin.buffer.readline

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    def next_index(x, y):
        if y % 2 == 0:
            if x == w - 1:
                return x, y + 1
            else:
                return x + 1, y
        else:
            if x == 0:
                return x, y + 1
            else:
                return x - 1, y

    ans = []
    x = 0; y = 0
    while True:
        next_x, next_y = next_index(x, y)

        if next_y == h:
            break

        if a[y][x] % 2 == 1:
            ans.append((y+1, x+1, next_y+1, next_x+1))
            a[next_y][next_x] += 1
        x = next_x; y = next_y

    print(len(ans))
    for i in ans:
        print(' '.join(map(str, i)))

main()