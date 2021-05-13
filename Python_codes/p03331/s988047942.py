def digitsum(s):
    su = 0
    for i in range(len(s)):
        su += int(s[i])

    return su

def main():
    N = int(input())

    ans = 10**10
    for a in range(1, N):
        b = N - a
        tmp = digitsum(str(a)) + digitsum(str(b))

        ans = min(ans, tmp)

    print(ans)

if __name__ == "__main__":
    main()