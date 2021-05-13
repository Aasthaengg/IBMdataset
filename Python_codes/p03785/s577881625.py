import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, c, k = MI()
    T = sorted([I() for _ in range(n)])
    cnt = 0
    i = 0
    while i < n:
        cnt += 1
        lim = T[i] + k
        cap = 1
        for j in range(i+1, min(n, i+c)):
            if T[j] <= lim:
                cap += 1
            else:
                break
        i += cap
    print(cnt)
if __name__ == '__main__':
    main()