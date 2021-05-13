def main():
    N = int(input())
    V = map(int, input().split())
    C = map(int, input().split())
    print(sum(max(0, v - c) for v, c in zip(V, C)))


if __name__ == '__main__':
    main()
