def main():
    from string import ascii_lowercase
    dic = {s: i for i, s in enumerate(ascii_lowercase)}
    rdic = {i: s for i, s in enumerate(ascii_lowercase)}
    N = int(input())
    ans = []

    def dfs(n, s):
        if N < n:
            return
        elif n == N:
            ans.append(s)
            return
        else:
            for i in range(max([dic[c] for c in s])+2):
                v = s + rdic[i]
                dfs(n+1, v)
    dfs(1, "a")
    ans.sort()
    print(*ans, sep="\n")


if __name__ == '__main__':
    main()
