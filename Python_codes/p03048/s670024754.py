def main():
    R, G, B, N = map(int, input().split())

    cnt = 0
    for r in range(N//R + 1):
        for b in range(N//B + 1):
            res = (N - r*R - b*B)
            if res >= 0 and res%G == 0:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()