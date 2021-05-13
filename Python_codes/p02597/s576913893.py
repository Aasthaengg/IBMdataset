# import sys
# readline = sys.stdin.readline
# generator = (readline().strip() for _ in range(N))

# N, M = map(int, input().split())
# As = list(map(int, input().split()))
# queries = (input() for _ in range(N))


def solve():
    N = int(input())
    stones = input()

    count = 0
    visited = 0
    r = stones[::-1]
    for i in range(N):
        if stones[i] == "W":
            j = r.find('R', visited, N-i)
            if j > -1:
                visited = j + 1
                count += 1

    return count


def main():
    print(solve())


if __name__ == "__main__":
    main()
