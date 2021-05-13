import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    s = input()
    L = len(s)
    ans = ''
    for i in range(0,L,2):
        ans += s[i]
    print(ans)

if __name__ == '__main__':
    main()
