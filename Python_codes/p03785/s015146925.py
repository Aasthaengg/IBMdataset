def main():
    N, C, K = map(int, input().split())
    T = []
    for _ in range(N):
        t = int(input())
        T.append(t)
    T.sort()

    busmintime = 0
    busmaxtime = K
    ans = 0
    cnt = 0
    i = 0
    for _ in range(N**2):
        busmintime = T[i]
        cnt += 1
        busmaxtime = busmintime + K
        for j in range(i+1, N):
            jtime = T[j]
            if jtime > busmaxtime or cnt == C:
                ans += 1
                cnt = 0
                i = j
                break
            cnt += 1
        if j == N-1:
            ans += 1
            break

    print(ans)

if __name__ == "__main__":
    main()
