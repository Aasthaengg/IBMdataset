from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    x, y = map(int, input().split())
    a = max(0, (4 - x) * 100000)
    b = max(0, (4 - y) * 100000)
    c = 400000 if x == y == 1 else 0
    print(a + b + c)

main()