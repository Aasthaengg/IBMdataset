import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

n,a,b = list(map(int, input().split()))
v = list(map(int, input().split()))
v.sort()

def sub(x):
    """x個の最大値・個数
    """
    val = (sum(v[-x:]), x)
    tmp = v[-x]
    n0 = 0
    n1 = 0
    for i in range(n-x, n):
        if v[-x]==v[i]:
            n1 += 1
        else:
            break
    for i in range(n-x-1, -1, -1):
        if v[-x]==v[i]:
            n0 += 1
        else:
            break
    # cmb(n0+n1, n1)
    num = 1
    for i in range(1,n1+n0+1):
        num *= i
    for i in range(1, n1+1):
        num //= i
    for i in range(1, n0+1):
        num //= i
    return val, num
ans = None
for x in range(a, b+1):
    val, num = sub(x)
    if ans is None:
        ans = (val, num)
    else:
        if ans[0][0]*val[1]==ans[0][1]*val[0]: # 0/1
            ans = (ans[0], num+ans[1])
        elif ans[0][0]*val[1]<ans[0][1]*val[0]:
            ans = (val, num)
ans = (ans[0][0]/ans[0][1], ans[1])
print("\n".join(map(str, ans)))