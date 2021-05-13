N = int(input())
seed = "a"
alpha = "abcdefghij"


def dfs(string, mx_ind):
    if len(string) == N:
        print(string)
    else:
        for i in range(mx_ind + 1):
            dfs(string + alpha[i], mx_ind + 1 if i == mx_ind else mx_ind)


dfs("", 0)
