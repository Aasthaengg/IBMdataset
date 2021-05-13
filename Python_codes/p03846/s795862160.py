import collections
def solve(n, a_list):

    count = collections.Counter()
    for a in a_list:
        count[a] += 1

    count[0] += 1
    c = [False] * n
    for k, v in count.items():
        c[k] = (v == 2)

    if n % 2 == 1:
        tmp = all([v for i, v in enumerate(c) if i % 2 == 0])
    else:
        tmp = all([v for i, v in enumerate(c) if i % 2 == 1])

    if tmp:
        return (2 ** (n//2) ) % (10**9+7)
    else:
        return 0

if __name__ == "__main__":
    n = int(input())
    a_list = [int(i) for i in input().split()]
    print(solve(n, a_list))
