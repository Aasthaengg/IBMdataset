def main():
    N = int(input())
    S = list(input().rstrip())
    ans = []
    for s in S:
        if ord(s) + N > 90:
            ans.append(chr(ord(s) + N - 26))
        else:
            ans.append(chr(ord(s) + N))
    print("".join(ans))


if __name__ == '__main__':
    main()
