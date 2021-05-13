def main():
    n,k = map(int,input().split())
    s = list(input())
    s[k - 1] = chr(ord(s[k - 1]) + 32)
    t = ''
    for i in s:
        t = t + i
    print(t)
main()