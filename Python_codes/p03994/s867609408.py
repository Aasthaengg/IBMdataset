import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    s = input()
    k = int(input())
    r = ""
    for se in s:
        if se == 'a':
            r += 'a'
        else:
            if 123 - ord(se) <= k:
                r += 'a'
                k -= (123 - ord(se))
            else:
                r += se
    if k:
        k = k % 26
        lastc = chr(k + ord(r[-1]))
        r = r[:-1] + lastc
    print(r)


if __name__ == '__main__':
    main()
