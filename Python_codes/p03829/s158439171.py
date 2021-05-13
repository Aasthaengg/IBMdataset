def main():
    n, a, b = map(int, input().split())
    x = tuple(map(int, input().split()))
    r = 0
    for i1 in range(1, n):
        dis = x[i1] - x[i1-1]
        if dis * a > b:
            r += b
        else:
            r += dis * a
    print(r)

if __name__ == '__main__':
    main()
