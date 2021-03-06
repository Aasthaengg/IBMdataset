
def resolve():
    N, D, A = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()

    # imos
    imos = [0] * (N+1)
    ans = 0
    R = 0
    for l in range(N):
        if l:
            imos[l] += imos[l - 1]
        x = AB[l][0]
        h = AB[l][1]
        if imos[l] < h:
            R = max(R, l + 1)
            while R < N and AB[R][0] <= 2 * D + x:
                R += 1
            d = h - imos[l]
            cnt = -(-d//A) # εγδΈγ
            imos[l] += cnt * A
            imos[R] -= cnt * A
            ans += cnt
    print(ans)

if __name__ == "__main__":
    resolve()