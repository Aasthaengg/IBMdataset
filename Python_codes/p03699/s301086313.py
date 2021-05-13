import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
inf = float('inf')
def main():
    n = I()
    s = [0]*n
    for i in range(n):
        s[i] = I()
    s_sum = sum(s)
    if s_sum%10 != 0:
        print(s_sum)
        sys.exit()
    s_min = inf
    for ss in s:
        if (ss%10 != 0) and (ss < s_min):
            s_min = ss
    if s_min == inf:
        print(0)
    else:
        print(s_sum-s_min)

if __name__ == '__main__':
    main()