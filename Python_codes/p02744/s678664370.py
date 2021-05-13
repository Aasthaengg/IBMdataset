def main():
    char_list = 'abcdefghijk'
    N = int(input())

    def dfs(s, n=N, n_char=0):
        if n == 0:
            print(s)
            return
        # 既出の文字
        for c in char_list[:n_char]:
            dfs(s + c, n - 1, n_char)
        # 新しい文字
        dfs(s + char_list[n_char], n - 1, n_char + 1)

    dfs('')


if __name__ == '__main__':
    main()