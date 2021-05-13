import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))

def main():
    s = IS()
    k = II()
    subs = []
    n = len(s)
    for i in range(k):
        for j in range(n-i):
            subs.append(s[j:j+(i+1)])
    subs = sorted(list(set(subs)))
    print(subs[k-1])

if __name__ == '__main__':
    main()
