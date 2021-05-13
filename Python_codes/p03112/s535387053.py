from bisect import bisect_right


def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    neighbour_temple = [[] for _ in range(a)]
    for i in range(a):
        idx = bisect_right(t, s[i])
        if idx == b:
            neighbour_temple[i].append(t[-1])
        else:
            if idx > 0:
                neighbour_temple[i].append(t[idx - 1])
            neighbour_temple[i].append(t[idx])
    for _ in range(q):
        begin = int(input())
        idx = bisect_right(s, begin)
        visit_s = []
        if idx == a:
            visit_s.append(a - 1)
        else:
            if idx > 0:
                visit_s.append(idx - 1)
            visit_s.append(idx)
        ans = float("inf")
        for v_s in visit_s:
            for v_t in neighbour_temple[v_s]:
                min_point = min(s[v_s], v_t)
                large_point = max(s[v_s], v_t)
                if min_point <= begin <= large_point:
                    ans = min(ans, large_point - min_point + min(begin - min_point, large_point - begin))
                elif begin <= min_point <= large_point:
                    ans = min(ans, abs(large_point - begin))
                else:
                    ans = min(ans, abs(min_point - begin))
        print(ans)


if __name__ == '__main__':
    main()
