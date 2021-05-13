import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
if k>max(a):
    ans = 0
elif k in a:
    ans = 1
elif n==1:
    if a[0]==k:
        ans = 1
    else:
        ans = 0
else:
    g = gcd(a[0], a[1])
    for num in a[2:]:
        g = gcd(g, num)
    if k%g==0:
        ans = 1
    else:
        ans = 0
ans = "POSSIBLE" if ans else "IMPOSSIBLE"
print(ans)