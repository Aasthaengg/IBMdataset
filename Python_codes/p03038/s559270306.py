def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n, m = map(int, input().split())
    from heapq import heappop, heappush, heapreplace
    a = list(map(int, input().split()))
    from collections import Counter as cc
    a = cc(a)
    q = []
    for key in a:
        heappush(q, (key, a[key]))
    for i in range(m):
        b, c = map(int, input().split())
        now = b
        while q:
            num, cnt = q[0]
            if c <= num: break
            
            if now >= cnt:
                now -= cnt
                heappop(q)
            else:
                heapreplace(q, (num, cnt-now))
                now = 0
                break
        if now != b:
            heappush(q, (c, b-now))
    ans = 0
    for num, cnt in q:
        ans += num*cnt
    print(ans)



if __name__ == '__main__':
    main()