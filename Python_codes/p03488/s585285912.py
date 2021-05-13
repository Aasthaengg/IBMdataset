def main():
    SFT = 8000

    CMDs = map(len, input().split('T'))
    X, Y = map(int, input().split())

    # [-SFT,SFT] -> [0,SFT*2]
    axis = 0
    curr = [1 << (next(CMDs) + SFT), 1 << SFT]
    for d in CMDs:
        axis ^= 1
        curr[axis] = (curr[axis] >> d) | (curr[axis] << d)

    cond = (curr[0] >> (SFT + X)) & 1 and (curr[1] >> (SFT + Y)) & 1
    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
