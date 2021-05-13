import sys
n = int(sys.stdin.readline().rstrip("\n"))
INF = float('inf')
ans = INF
for a in range(1,(n+2)//2):
    b = n-a
    s = 0
    while a != 0:
        a,p = divmod(a, 10)
        s += p
    while b != 0:
        b,p = divmod(b, 10)
        s += p
    ans = min(ans,s)
print(ans)