import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    cnt_w = [0]*(len(S) + 1)
    for i in range(len(S) - 1,-1,-1):
        if S[i] == 'W':
            cnt_w[i] = cnt_w[i + 1] + 1
        else:
            cnt_w[i] = cnt_w[i + 1]
    ans = 0
    for i in range(len(S)):
        if S[i] == 'B':
            ans += cnt_w[i]
    print(ans)
if __name__ == '__main__':
    main()