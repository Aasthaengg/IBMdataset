def main():
    from sys import stdin
    input = stdin.readline
    h, w, n = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0]*n]

    ans = [0]*10
    d = {}

    for a, b in ab:
        for j in range(-1, 2):
            for k in range(-1, 2):
                d[(a+j, b+k)] = d.get((a+j, b+k), 0)+1

    for (i, j), k in d.items():
        if 2 <= i < h and 2 <= j < w:
            ans[k] += 1

    print((h-2)*(w-2)-sum(ans))
    for i in ans[1:]:
        print(i)


main()