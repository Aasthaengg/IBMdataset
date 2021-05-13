def cnt(a):
    res = 0
    while not a%2:
        res += 1
        a //= 2
    return res
N = int(input())
res = 0
for a in map(int, input().split()):
    res += cnt(a)
print(res)