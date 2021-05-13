def main():
    import sys
    input = sys.stdin.readline
    S = input().strip()
    p = ''
    c = ''
    ans = 0
    for s in S:
        c += s
        if p != c:
            ans += 1
            p = c
            c = ''
        
    print(ans)

if __name__ == '__main__':
    main()