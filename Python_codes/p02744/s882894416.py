def main():
    from string import ascii_lowercase
    N = int(input())
    ascii_dic = {i: a for i, a in enumerate(ascii_lowercase)}
    ascii_rdic = {a: i for i, a in enumerate(ascii_lowercase)}
    # ans = []

    def dfs(A):
        if len(A) == N:
            # ans.append("".join(A))
            print("".join(A))
            return
        if not A:
            dfs(["a"])
        else:
            s = max(ascii_rdic[a] for a in A)
            for i in range(s+2):
                dfs(A + [ascii_dic[i]])

    dfs([])

    # for i in range(len(ans)):
    #     for j in range(i+1, len(ans)):
    #         S = ans[i]
    #         T = ans[j]
    #         same = True  # 同型である
    #         for k in range(N):
    #             for m in range(k, N):
    #                 if not ((S[k] == S[m] and T[k] == T[m]) or
    #                         (S[k] != S[m] and T[k] != T[m])):
    #                     same = False
    #         if same:  # 同型である
    #             print(S, T)


if __name__ == '__main__':
    main()
