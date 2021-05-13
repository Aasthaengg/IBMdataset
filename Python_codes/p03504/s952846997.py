import sys
input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    stc = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: (x[2], x[0])) + [[1, 1, 31]]
    # print(stc)
    imos = [0] * (int(1e5) + 10)
    s, t, c = stc[0]
    pre_s, pre_t, pre_c = s, t, c
    for i in range(1, N+1):
        s, t, c = stc[i]
        if c == pre_c and pre_t == s:
            pre_t = t
        else:
            imos[pre_s] += 1
            imos[pre_t + 1] -= 1
            pre_s, pre_t, pre_c = s, t, c
    # print(imos[:100])

    ans = 0
    tmp = 0
    for i in imos:
        tmp += i
        ans = max(ans, tmp)
    print(ans)

if __name__ == "__main__":
    main()