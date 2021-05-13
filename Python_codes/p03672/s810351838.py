def solve():
    S = input()
    for _ in range(len(S)):
        S = S[:-2]
        if S[:len(S) // 2] == S[len(S) // 2:]:
            print(len(S))
            exit()


if __name__ == "__main__":
    solve()
