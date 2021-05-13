def main():
    R, G, B, N = map(int, input().split())

    cnt = 0
    for r in range(N//R+1):
        if r*R > N: break
        for g in range(N//G+1):
            if r*R + g*G > N: break
            res = N - (r*R+g*G)
            if res % B == 0:
                cnt += 1
    print(cnt)

main()