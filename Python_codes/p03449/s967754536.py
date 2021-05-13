n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

res = 0
for i in range(1,n+1):
    aa = sum(al[:i])
    bb = sum(bl[i-1:])
    res = max(res,aa+bb)

print(res)