def solve():
    if len(S) < len(T):
        print('UNRESTORABLE')
        return

    valid_strs = []
    for i in range(len(S)):
        for j in range(len(T)):
            if len(S) <= i + j or S[i + j] != '?' and S[i + j] != T[j]:
                break
        else:
            valid_strs.append((S[: i] + T + S[i + len(T): ]).replace('?', 'a'))
    print(min(valid_strs) if valid_strs else 'UNRESTORABLE')

if __name__ == "__main__":
    S = input()
    T = input()
    solve()