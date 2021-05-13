def main():
    R, G, B, N = map(int, input().split())
    ans = 0

    for r in range(N//R + 1):
        for g in range(N//G + 1):

            res = (N - (R*r + G*g)) 

            if res < 0 :
                break

            if res % B == 0:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()