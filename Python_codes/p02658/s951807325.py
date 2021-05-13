n = int(input())
v = [int(i) for i in input().split()]
if v.count(0) > 0:
    print(0)
    exit(0)
res = 1
for i in v:
    res *= i
    if (res > 10**18):
        print(-1)
        exit(0)
print(res)
