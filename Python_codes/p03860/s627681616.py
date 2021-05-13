from sys import stdin
def LS(): return list(stdin.readline().rstrip().split())
ls = LS()
a,b,c = [ls.pop(0) for i in range(3)]

ans = a[0] + b[0] + c[0]

print(ans)