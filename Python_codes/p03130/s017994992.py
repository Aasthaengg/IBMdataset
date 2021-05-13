def main():
    N = 4
    edge = [[] for _ in range(N)]
    for i in range(N-1):
        a, b = (int(i) for i in input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    even, odd = 0, 0
    for e in edge:
        if len(e) % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd == 2 and even == 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
