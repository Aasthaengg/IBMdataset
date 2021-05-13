def dfs(word, N):
    if len(word) == N:
        print(word)
    else:
        for i in range(len(set(word))+1):
            dfs(word + chr(97+i), N)


def main():
    N = int(input())
    dfs('a', N)


if __name__ == "__main__":
    main()
