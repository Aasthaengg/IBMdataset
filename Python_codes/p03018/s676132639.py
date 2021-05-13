import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()


def resolve():
    s = str(input())
    s = s.replace('BC', 'D')
    ans = a = 0
    for i in s:
        if i == 'A':
            a += 1
        elif i == 'D':
            ans += a
        else:
            a = 0
    print(ans)


resolve()