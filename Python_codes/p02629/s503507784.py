def solve():
    # ref. https://drken1215.hatenablog.com/entry/2020/06/21/225500
    N = int(input())
    ans = ''
    while N > 0:
        N -= 1
        N,digit = divmod(N,26)
        ans += chr(ord('a') + digit)
    print(ans[::-1])

if __name__ == "__main__":
    solve()