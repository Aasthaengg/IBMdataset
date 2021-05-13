def main():
    N = int(input())
    P = [int(_) for _ in input().split()]

    i = 1
    output = 0
    while i <= N:
        if i == P[i-1]:
            output += 1
            if i < N and i+1 == P[i]:
                i += 2
                continue
        i += 1
    print(output)
    return

if __name__ == '__main__':
    main()
