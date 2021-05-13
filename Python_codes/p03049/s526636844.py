MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    cnt = 0
    ba = 0
    a = 0
    b = 0
    for s in S:
        for i in range(len(s) - 1):
            if s[i] == 'A' and s[i + 1] == 'B':
                cnt += 1
        if s[0] == 'B' and s[-1] == 'A':
            ba += 1
        elif s[0] == 'B':
            b += 1
        elif s[-1] == 'A':
            a += 1
    
    if a > 0 and b > 0:
        cnt += ba + 1 + min(a - 1,b - 1)
    elif a > 0:
        cnt += ba
    elif b > 0:
        cnt += ba
    else:
        if ba > 0:
            cnt += ba - 1
    print(cnt)
if __name__ == '__main__':
    main() 