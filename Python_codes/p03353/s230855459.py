import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import defaultdict
def main():
    s = list(input())
    k = int(input())
    k -= 1

    d1 = defaultdict(list)
    for i, c in enumerate(s):
        d1[c].append(i)
    d2 = sorted(d1.items())

    lens = len(s)
    for d2e in d2:
        subs = set()
        subs.add(d2e[0])
        for d2ee in d2e[1]:
            end = min(lens + 1, d2ee + k + 2)
            for i1 in range(d2ee+1, end):
                subs.add("".join(s[d2ee:i1]))
        if len(subs) > k:
            subsl = list(subs)
            subsl.sort()
            print(subsl[k])
            sys.exit()
        else:
            k -= len(subs)

if __name__ == '__main__':
    main()