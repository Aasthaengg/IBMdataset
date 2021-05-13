def main():
    N, M = map(int, input().split())
    bridge_count = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        bridge_count[a] += 1
        bridge_count[b] += 1
    for i in range(N):
        print(bridge_count[i])

if __name__ == "__main__":
    main()
