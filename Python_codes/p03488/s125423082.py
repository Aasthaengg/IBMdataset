def main():
    *CMDs, = map(len, input().split('T'))
    X, Y = map(int, input().split())

    X -= CMDs[0]  # この操作だけは対称性がない

    def is_reachable(cmds, goal):
        SFT = 8000
        # [-SFT,SFT] -> [0,SFT*2]
        dp = 1 << SFT
        for d in cmds:
            dp = (dp >> d) | (dp << d)
        return SFT + goal >= 0 and (dp >> (SFT + goal)) & 1  # negative_shiftでRE

    cond = is_reachable(CMDs[2::2], X) and is_reachable(CMDs[1::2], Y)
    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()

# RE
# CMDs = [8000, 0]
# X, Y = -8000, 0
