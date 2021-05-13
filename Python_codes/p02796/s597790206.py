def main():
    N = int(input())
    X = []
    for _ in range(N):
        x, l = (int(_) for _ in input().split())
        X.append([x-l, x+l])
    X.sort(key=lambda x:x[1])
    output = 0
    last = -10 ** 12
    for i in range(N):
        if last <= X[i][0]:
            output += 1
            last = X[i][1]
    print(output)
    return

if __name__ == '__main__':
    main()
