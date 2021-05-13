import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    t = [["#"] * 100 for _ in range(50)] + [["."] * 100 for _ in range(50)]
    w, b = map(int, input().split())
    w, b = w - 1, b - 1
    br = False
    for i in range(0, 50, 2):
        for j in range(0, 100, 2):
            if w == 0:
                br = True
                break
            t[i][j] = "."
            w -= 1
        if br: break
    br = False
    for i in range(51, 100, 2):
        for j in range(0, 100, 2):
            if b == 0:
                br = True
                break
            t[i][j] = "#"
            b -= 1
        if br: break
    print(100, 100)
    for x in t:
        print(*x, sep="")

main()
