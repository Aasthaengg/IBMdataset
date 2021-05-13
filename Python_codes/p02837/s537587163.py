import sys
input = sys.stdin.readline

def main():
    # 証言が矛盾していないかチェックする
    def check(bit):
        for i in range(n):
            if not bit & (1 << i):
                continue

            for human, is_honest in a[i]:
                if is_honest == 1 and (bit & (1 << human)):
                    continue
                elif is_honest == 0 and not (bit & (1 << human)):
                    continue
                else:
                    return False
        return True

    n = int(input())
    ans = 0
    a = [[] for _ in range(n)]
    for i in range(n):
        m = int(input())
        for j in range(m):
            xy = list(map(int, input().split()))
            xy[0] -= 1
            a[i].append(xy)

    # 全パターン回す
    for bit in range((1 << n)):
        num = 0
        if check(bit):
            for k in range(n):
                if bit & (1 << k):
                    num += 1
            ans = max(ans, num)
    print(ans)

if __name__ == '__main__':
    main()
