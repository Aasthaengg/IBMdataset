def main():
    S = input()
    N = len(S)
    if S == "keyence":
        print("YES")
        return
    for i in range(N):
        for j in range(i + 1, N + 1):
            cand = S[:i] + S[j:]
            if cand == "keyence":
                print("YES")
                return

    print("NO")
    return


main()
