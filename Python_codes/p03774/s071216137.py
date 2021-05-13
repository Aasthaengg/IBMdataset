import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N,M = [int(i) for i in input().strip().split()]
    students = [[int(i) for i in input().strip().split()] for _ in range(N)]
    checkpoints = [[int(i) for i in input().strip().split()] for _ in range(M)]
    ans = [0] * N

    for i,student in enumerate(students):
        dist = [float("inf")] * M
        for j, checkpoint in enumerate(checkpoints):
            dist[j] = abs(student[0] - checkpoint[0]) + abs(student[1] - checkpoint[1])
        ans[i] = dist.index(min(dist)) + 1

    return ans


if __name__ == "__main__":
    for n in main():
        print(n)
