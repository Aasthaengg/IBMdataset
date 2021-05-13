import sys
input = sys.stdin.readline

def main():
    n = int(input())
    plus = []
    minus = []
    for _ in range(n):
        x, y = map(int, input().split())
        plus.append(x + y)
        minus.append(x - y)
    plus.sort()
    minus.sort()
    ans = max(plus[-1] - plus[0], minus[-1] - minus[0])
    print(ans)

main()