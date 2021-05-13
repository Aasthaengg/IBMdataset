alpha = list("abcdefghij")


def dfs(v, depth):
    if depth == N:
        print(v)
        return
    if depth <= N:
        for next_ in alpha[: len(set(list(v))) + 1]:
            dfs(v + next_, depth + 1)


if __name__ == "__main__":
    N = int(input())

    dfs("a", depth=1)
