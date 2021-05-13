def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    seats = [0]*(10**5+2)
    LR = [[int(i) for i in input().split()] for j in range(N)]
    for li, ri in LR:
        seats[li] += 1
        seats[ri+1] -= 1
    from itertools import accumulate
    S = list(accumulate(seats))
    print(sum(S))


if __name__ == '__main__':
    main()
