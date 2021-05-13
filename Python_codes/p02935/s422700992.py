def main():
    N = int(input())
    V = list(map(int, input().split()))
    while len(V) > 1:
        V.sort()
        new_v = sum(V[0:2]) / 2
        V = V[2:]
        V.append(new_v)
    print(V[0])


if __name__ == '__main__':
    main()
