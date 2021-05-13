import sys
a,b = map(int, sys.stdin.readline().rstrip("\n").split())
ans = 0
for i in range(a,b+1):
    i,n1 = divmod(i, 10)
    i,n2 = divmod(i, 10)
    i,n3 = divmod(i, 10)
    n5,n4 = divmod(i, 10)
    if n1 == n5 and n2 == n4:
        ans += 1
print(ans)