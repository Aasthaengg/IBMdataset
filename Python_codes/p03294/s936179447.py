N = input().rstrip()
res = 0
for a in map(int, input().split()):
    res += a-1
print(res)