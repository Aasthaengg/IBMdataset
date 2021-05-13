def solve():
    s = input()
    s3 = [int(s[i:i+3]) for i in range(len(s) - 2)]
    ans = 1000000
    for n in s3:
        ans = min(ans, abs(753 - n))
    print(ans)


if __name__ == '__main__':
    solve()
