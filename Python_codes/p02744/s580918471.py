import sys
sys.setrecursionlimit(10 ** 9)
if __name__ == '__main__':
    def solve(s, a):
        if len(s) == n:
            print(s)
        else:
            for c in range(ord("a"), a + 1):
                if c == a:
                    solve(s + chr(c), a + 1)
                else:
                    solve(s + chr(c), a)
    n = int(input())
    solve("", ord("a"))

