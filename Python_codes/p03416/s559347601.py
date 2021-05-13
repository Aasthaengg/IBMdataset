import sys
def input(): return sys.stdin.readline().strip()


def main():
    a, b = map(int, input().split())
    ans = 0
    for n in range(a, b + 1):
        c = str(n)
        l = len(c)
        circle = True
        for i in range(l // 2):
            if c[i] != c[-i-1]:
                circle = False
                break
        if circle: ans += 1
    print(ans)

if __name__ == "__main__":
    main()
