def main():
    S = input()
    ans = 0
    for n in range(2**(len(S)-1)):
        fig = S[0]
        index = 1
        for _ in range(len(S)-1):
            if n % 2:
                fig += "+"+S[index]
            else:
                fig += S[index]
            n >>= 1
            index += 1
        ans += eval(fig)
    print(ans)


if __name__ == "__main__":
    main()
