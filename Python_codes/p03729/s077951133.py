#ABC060 A - Shiritori
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
a,b,c = map(str, input().split())
if a[-1]==b[0] and b[-1]==c[0]:
    print('YES')
else:
    print('NO')
