def main():
    N, M = (int(_) for _ in input().split())
    a = []
    output = 0
    for p in range(1, int(M**.5)+1):
        if M%p == 0:
            a.append(p)
            a.append(M//p)
    for p in a:
        if M//p >= N: output = max(output, p)
    print(output)
    return

if __name__ == '__main__':
    main()
