import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    BX = 0
    XA = 0
    BA = 0
    AB = 0
    for _ in range(N):
        S = readline().decode('utf-8').strip()
        if S[0]=='B' and S[-1]=='A':
            BA += 1
        elif S[0]=='B':
            BX += 1
        elif S[-1] == 'A':
            XA += 1
        AB += S.count('AB')
    if BA==0:
        ans = AB + min(BX,XA)
    else:
        if XA+BX>0:
            ans = AB + BA + min(BX, XA)
        else:
            ans = AB + BA-1
    print(ans)
if __name__ == '__main__':
    main()