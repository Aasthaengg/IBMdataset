def main():
    R, G, B, N = map(int, input().split())

    cnt = 0
    for r in range(N//R+1):
        for g in range(N//G+1):
            res = N - (r*R+g*G)
            if res >= 0 and res % B == 0:
                cnt += 1
    print(cnt)

main()