def main():
    N = int(input())
    S = input()
    RGB = [0]*3
    for s in S:
        if s == "R":
            RGB[0] += 1
        elif s == "G":
            RGB[1] += 1
        else:
            RGB[2] += 1
    ans = RGB[0] * RGB[1] * RGB[2]
    for d in range(1, N):
        for i in range(N-d+1):
            if N <= i + 2*d:
                break
            if S[i] != S[i+d] and S[i] != S[i+2*d] and S[i+d] != S[i+2*d]:
                ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
