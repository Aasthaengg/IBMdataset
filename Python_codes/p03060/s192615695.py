import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(1 << N):
        value = 0
        cost = 0
        for j in range(N):
            if i & (1 << j):
                value += V[j]
                cost += C[j]
        ans = max(ans, value - cost)
    print(ans)




if __name__ == "__main__":
    main()
