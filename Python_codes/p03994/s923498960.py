def main():
    S = list(input())
    k = int(input())
    ans = []
    for s in S:
        if s != 'a' and ord(s) >= 123 - k:
            ans.append('a')
            k -= 123 - ord(s)
        else:
            ans.append(s)
    if k > 0:
        ans[-1] = chr((ord(ans[-1]) + k - 97) % 26 + 97)
    print(''.join(ans))

if __name__ == '__main__':
    main()
