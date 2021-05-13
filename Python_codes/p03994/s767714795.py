def main():
    S = input()
    K = int(input())
    ans = ['' for _ in range(len(S))]
    for i in range(len(S)):
        d = ord(S[i]) - ord('a')
        shift = (26 - d) % 26
        if K - shift >= 0:
            ans[i] = 'a'
            K -= shift
        else:
            ans[i] = S[i]
    if K > 0:
        K %= 26
        d = (K + ord(ans[-1]) - ord('a')) % 26
        ans[-1] = chr(d + ord('a'))
    print(''.join(ans))


if __name__ == '__main__':
    main()