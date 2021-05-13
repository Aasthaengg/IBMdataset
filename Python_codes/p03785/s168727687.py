def main():
    N, C, K = map(int, input().split())
    T = list()

    for i in range(N):
        T.append(int(input()))
    T = sorted(T)

    ans = 0
    cap = 0
    t0 = T[0]

    for i in range(N):
        if T[i] <= t0 + K:
            if cap + 1 <= C:
                cap += 1
            else:
                ans += 1
                t0 = T[i]
                cap = 1
            
        else:
            ans += 1
            t0 = T[i]
            cap = 1

    if cap > 0:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()