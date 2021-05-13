def solve():
    S = input()
    T = input()
    for _ in range(len(S)):
        if T == S:
            print('Yes')
            exit()
        S = S[1:] + S[0]
    print('No')

if __name__ == "__main__":
    solve()