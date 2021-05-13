def main():
    S = list(input())
    r = 0

    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            r += 1

    S.reverse()
    l = 0

    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            l += 1        

    print(min(r, l))
if __name__ == "__main__":
    main()