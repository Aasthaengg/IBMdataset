def resolve():
    from collections import defaultdict
    N = int(input())
    A = [int(i) for i in input().split()]
    dic = defaultdict(int)
    for a in A:
        dic[a] += 1
    ans = 0
    for k, v in dic.items():
        if k <= v:
            ans += v - k
        else:
            ans += v
    print(ans)


resolve()
