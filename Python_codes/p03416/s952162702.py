def solve():
    ans = 0
    A, B = [int(i) for i in input().split()]
    for i in range(A, B + 1):
        s = str(i)
        l = len(s)
        if all(s[j] == s[l - 1 - j] for j in range(int(l / 2))):
            ans += 1
    print(ans)

if __name__ == "__main__":
    solve()