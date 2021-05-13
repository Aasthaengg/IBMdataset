import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    S = input()
    L = len(S)
    ans = 'NO'
    for i in range(0,8):
        s = S[:i] + S[L-7+i:]
        if s == 'keyence':
            ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()