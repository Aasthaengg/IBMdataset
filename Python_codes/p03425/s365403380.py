from collections import defaultdict
from itertools import combinations
def main():
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        s = input()
        d[s[0]] += 1
    ans = 0
    for i, j, k in combinations('MARCH', 3):
        ans += d[i] * d[j] * d[k]
    print(ans)

if __name__ == '__main__':
    main()
