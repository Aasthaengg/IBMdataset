import sys

input = sys.stdin.readline


class AtCoder:
    def main(self):
        N, K = map(int, input().split())

        max_pair = (N - 1) * (N - 2) // 2
        if K > max_pair:
            print(-1)
            exit()

        star = []
        for i in range(1, N):
            star.append((i, N))

        leaves = []
        for i in range(1, N):
            for j in range(1, i):
                leaves.append((i, j))

        star += leaves[:max_pair - K]
        print(len(star))
        for pair in star:
            print(" ".join(map(str, pair)))


# Run main
if __name__ == '__main__':
    AtCoder().main()
