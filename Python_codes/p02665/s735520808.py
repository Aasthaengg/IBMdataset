# import sys
# readline = sys.stdin.readline
# generator = (readline().strip() for _ in range(N))

# N, M = map(int, input().split())
# As = list(map(int, input().split()))
# queries = (input() for _ in range(N))


def solve():
    N = int(input())
    As = list(map(int, input().split()))

    if N > 0 and As[0] != 0:
        return -1
    if N == 0 and As[0] != 1:
        return -1        

    vertices = [1] * (N+1)
    previous = 0
    for i, a in enumerate(As[:0:-1]):
        max_n_vert = a + previous
        previous = max_n_vert
        vertices[N-i] = max_n_vert

    n_not_leaves_prev = 1
    for i, a in enumerate(As):
        if i == 0:
            continue
        # if n_not_leaves_prev == 0:
        #     return -1

        max_n_vert = 2 * n_not_leaves_prev
        vertices[i] = min(vertices[i], max_n_vert)
        n_not_leaves_prev = vertices[i] - a

        if max_n_vert < a:
            return -1

    return sum(vertices)


def main():
    print(solve())


if __name__ == "__main__":
    main()
