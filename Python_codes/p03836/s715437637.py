def main():
    sx, sy, tx, ty = list(map(int, input().split(' ')))
    assert sx < tx and sy < ty
    # s -> t
    ans = 'R' * (tx - sx) + 'U' * (ty - sy)
    # t -> s
    ans += 'L' * (tx - sx) + 'D' * (ty - sy)
    # s -> t
    ans += 'D' + 'R' * (tx - sx + 1) + 'U' * (ty - sy + 1) + 'L'
    # t -> s
    ans += 'U' + 'L' * (tx - sx + 1) + 'D' * (ty - sy + 1) + 'R'
    print(ans)


if __name__ == '__main__':
    main()