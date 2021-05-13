import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    card = [input() for _ in range(3)]
    idx = [0] * 3
    now = 0
    ans = None
    while True:
        if idx[now] >= len(card[now]):
            ans = chr(now + 65)
            break
        idx[now] += 1
        now = ord(card[now][idx[now] - 1]) - ord('a')
    print(ans)

if __name__ == '__main__':
    main()
