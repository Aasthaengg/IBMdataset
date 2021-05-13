def solve(V, G):
    ans = 0
    for i in range(V - 1):
        for j in range(i + 1, V):
            direct = G[i][j]
            for k in range(V):
                if k == i or k == j:
                    continue
                ind = G[i][k] + G[k][j]
                if direct > ind:
                    return -1
                elif direct == ind:
                    break
            else:
                ans += direct
    return ans


def main():
    V = int(input())
    G = [[int(i) for i in input().split()] for i in range(V)]
    print(solve(V, G))


if __name__ == "__main__":
    main()