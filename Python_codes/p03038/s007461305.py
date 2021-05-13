def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    from collections import Counter as cc
    a = cc(a)
    q = [(key, a[key]) for key in a]
    for i in range(m):
        b, c = map(int, input().split())
        q.append((c,b))
    q.sort(reverse=True)
    acc = 0
    ans = 0
    for num, cnt in q:
        if acc + cnt >= n:
            cnt = n-acc
            ans += num*cnt
            break
        acc += cnt
        ans += num*cnt
    print(ans)



if __name__ == '__main__':
    main()