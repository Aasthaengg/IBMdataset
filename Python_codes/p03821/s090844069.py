def main():
    N = int(input())
    A = list()

    for i in range(N):
        a, b = map(int, input().split())
        A.append([a, b])

    A.reverse()
    ans = 0
    offset = 0

    for pair in A:
        a, b = pair

        if (a + offset) % b == 0:
            n = 0
        else:
            n = b - ((a + offset) % b)

        ans += n
        offset += n
        
    print(ans)

if __name__ == "__main__":
    main()