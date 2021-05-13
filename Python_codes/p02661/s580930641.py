def main(N, lines):
    a = sorted(map(lambda line: line[0], lines))
    b = sorted(map(lambda line: line[1], lines))

    if N % 2 == 1:
        mi = a[N // 2]
        ma = b[N // 2]
        print(int(ma - mi + 1))
    else:
        mi = (a[N // 2 - 1] + a[N // 2])
        ma = (b[N // 2 - 1] + b[N // 2])
        print(int(ma - mi + 1))


N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))
main(N, lines)
