def main():
    N = int(input())
    playlist = list()

    for _ in range(N):
        title, time = input().split()
        playlist.append([title, int(time)])

    st = input()
    add_flag = 0
    ans = 0

    for p in playlist:

        if add_flag:
            ans += p[1]

        if p[0] == st:
            add_flag = 1

    print(ans)

if __name__ == "__main__":
    main()