import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    S = input()
    L = len(S)
    pre = ''
    s = ''
    ans = 0
    for i in range(L):
        s += S[i]
        if s!=pre:
            ans += 1
            pre = s
            s = ''
    print(ans)




if __name__ == '__main__':
    main()