#!python3

# input
N, M = list(map(int, input().split()))

# odd
def solve1():
    return [(i + 2, N - i) for i in range(M)]        


# even
def solve2():
    t = (N - 2) // 4
    l = [(i + 2, N - i) for i in range(t)]
    n = (N - 2) // 2 - t
    l = l + [(N // 2 + 1 + i, N // 2 - i) for i in range(n)]
    return l[:M]


def main():
    l = solve1() if N % 2 else solve2()
    for ans in l:
        print(*ans)
    

if __name__ == "__main__":
    main()
