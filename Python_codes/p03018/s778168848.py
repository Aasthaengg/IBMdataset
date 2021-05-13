import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    ans = 0
    stack = []
    for c in input():
        if len(stack) >= 2 and stack[-2:] == ["A", "B"] and c == 'C':
            ans += len(stack) - 1
            stack.pop()
        elif len(stack) >= 1 and stack[-1] == 'A' and c in ('A', 'B'):
            stack.append(c)
        elif c == 'A':
            stack = ['A']
        else:
            stack = []
    print(ans)
resolve()