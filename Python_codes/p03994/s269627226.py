def main():
    S = input()
    K = int(input())
    ans = ''
    for s in S:
        if 123 - ord(s) <= K and s != 'a':
            ans += 'a'
            K -= 123-ord(s)
        else:
            ans += s
    if K > 0:
        ans = ans[:-1] + chr((ord(ans[-1])+K-97) % 26+97)
    print(ans)


if __name__ == "__main__":
    main()
