def main():
    N = int(input())
    D, X = map(int, input().split())
    l = []
    for i in range(N):
        l.append(int(input()))
    choco = 0
    for i in range(N):
        day = 1
        choco += 1
        multiply = 1
        while day <= D:
            day = l[i] * multiply + 1
            if day > D:
                break
            else:
                choco += 1
                multiply += 1
    print(choco + X)

main()