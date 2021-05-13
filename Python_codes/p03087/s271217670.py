import bisect
def main():
    N, Q = map(int, input().split())
    S = input()
    ll = []
    t = -1
    for i, v in enumerate(S):
        if v == 'A':
            t = i
        elif v == 'C':
            if t == i-1:
                ll.append(i)
                t = -1
    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        li = bisect.bisect_right(ll, l)
        ri = bisect.bisect_right(ll, r)
        print(ri-li)
main()
