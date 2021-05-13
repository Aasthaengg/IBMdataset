def main():
    n, k = map(int, input().split())
    s = list(str(input()))
    s[k - 1] = s[k - 1].lower()
    w = ''
    for i in s:
        w = w + i
    print(w)
main()