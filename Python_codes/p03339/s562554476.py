import sys
read = sys.stdin.read
from itertools import accumulate
def main():
    n = int(input())
    s = list(input())

    if n == 2:
        if s[0] == 'E' or s[1] == 'W':
            print(0)
            sys.exit()
        else:
            print(1)
            sys.exit()
    e = [0] * n
    w = [0] * n
    for i1 in range(n):
        e[i1] = 1 if s[i1] == 'E' else 0
        w[i1] = 1 if s[i1] == 'W' else 0
    e.insert(0, 0)
    e.append(0)
    w.insert(0, 0)
    w.append(0)

    ea = list(accumulate(e))
    wa = list(accumulate(w))
    rt = n
    for j1 in range(1, n+1):
        rt = min(rt, wa[j1 - 1] + (ea[-1] - ea[j1]))
    print(rt)

if __name__ == '__main__':
    main()