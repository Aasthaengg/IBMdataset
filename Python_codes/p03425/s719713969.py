def main():
    n = int(input())
    S= []
    from collections import defaultdict
    import itertools
    D = defaultdict(int)
    for _ in range(n):
        s = input()
        D[s[0]] += 1

    L = ['M','A','R','C','H']
    ans = 0
    for p in list(itertools.combinations(L,3)):
        t = 1
        for i in p:
            t *= D[i]
        ans += t
    print(ans)

main()