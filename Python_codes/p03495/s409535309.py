import sys
from collections import Counter
def main():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))

    col = max(0, len(set(a)) - k)
    if col == 0:
        print(0)
        sys.exit()

    ac = Counter(a)
    acl = ac.most_common()[::-1]
    acll = [ace[1] for ace in acl[:col]]

    r = sum(acll)
    print(r)

if __name__ == '__main__':
    main()
