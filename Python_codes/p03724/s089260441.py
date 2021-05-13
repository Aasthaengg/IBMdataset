
def resolve():
    N, M = map(int, input().split())

    CNT = [0] * N
    for _ in range(M):
        x, y = map(lambda x: int(x) - 1, input().split())
        CNT[x] += 1
        CNT[y] += 1

    for c in CNT:
        if c % 2 == 1:
            print("NO")
            return
    else:
        print("YES")


if __name__ == "__main__":
    resolve()