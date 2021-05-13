def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    PY = {}
    for i in range(1, M+1):
        p, y = map(int,input().split())
        if p not in PY.keys():
            PY[p] = []
        PY[p].append((y, i))
    numbers = [0] * (1+M)
    for p in PY.keys():
        PY[p].sort(reverse=True)
        rank = 1
        while PY[p]:
            year, i = PY[p].pop()
            num = str(p).zfill(6) + str(rank).zfill(6)
            rank += 1
            numbers[i] = num
            
    for i in range(1, M+1):
        print(numbers[i])


main()