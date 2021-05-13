def main():
    n, a, b, c, d = map(int, input().split())
    s = input()
    r = 'Yes'
    if ('##' in s[a-1:c]) or ('##' in s[b-1:d]):
        r = 'No'
    else:
        if (c>d) and not ('...' in s[b-2:d+1]):
            r = 'No'
    print(r)

main()