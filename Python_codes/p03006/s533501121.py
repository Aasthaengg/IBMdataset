def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    if N == 1:
        print(1)
        exit()
    XY = [0] * N
    for i, (x, y) in enumerate([[int(x) for x in input().strip().split()] for _ in range(N)]):
        XY[i] = (x, y)
    XY.sort(key=lambda x:(x[0], x[1]))

    dic = defaultdict(int)
    for d in range(1, N):
        for i in range(N-d):
            dic[(XY[i+d][0]-XY[i][0], XY[i+d][1]-XY[i][1])] += 1
            dic[(XY[i][0]-XY[i+d][0], XY[i][1]-XY[i+d][1])] += 1

    print(N-max(dic.values()))

if __name__ == '__main__':
    main()