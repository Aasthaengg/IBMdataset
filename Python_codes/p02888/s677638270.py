import sys
input = sys.stdin.readline

def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    ans = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            L = j
            R = n
            ij = l[i] + l[j]
            while R - L != 1:
                if ij <= l[j + 1]:
                    break
                now = (L + R)//2
                if ij > l[now]: #三角形になる
                    L = now
                else:
                    R = now
            ans += L - j

    print(ans)

main()