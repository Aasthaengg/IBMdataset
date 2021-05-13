if __name__ == "__main__":
    n = int(input())
    s = []
    ans = 0
    now = 1
    for i in range(n):
        s.append(int(input()))
    for i in s:
        now = s[now-1]
        ans += 1
        if now == 2:
            print(ans)
            break
    else:
        print(-1)