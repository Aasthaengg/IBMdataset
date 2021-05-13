def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    s = input()
    n = len(s)
    ans = [0]*(n)
    d = []
    s += '.'
    cnt = 0
    for i in range(n):
        cnt += 1
        if s[i] != s[i+1]:
            d.append((cnt,i))
            cnt = 0
    for i in range(0, len(d),2):
        cnt1, idx1 = d[i]
        cnt2, _ = d[i+1]
        ans[idx1] = cnt1 + cnt2//2 - cnt1//2
        ans[idx1+1] = cnt2 + cnt1//2 - cnt2//2
    print(*ans)


if __name__ == '__main__':
    main()