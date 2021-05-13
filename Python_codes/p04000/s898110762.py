def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    from itertools import product

    h, w, n = map(int, input().split())
    dic = {}
    for _ in range(n):
        a, b = map(int, input().split())
        a -= 2
        b -= 2
        for i in product([-1, 0, 1], repeat=2):
            aa = a + i[0]
            bb = b + i[1]
            if 0 <= aa <= h-3 and 0 <= bb <= w-3:
                try:
                    dic[(aa, bb)] += 1
                except:
                    dic[(aa, bb)] = 1

    ans = [0] * 10
    for i in dic.values():
        ans[i] += 1
    ans[0] = (h-2) * (w-2) - len(dic)

    for i in ans:
        print(i)

main()