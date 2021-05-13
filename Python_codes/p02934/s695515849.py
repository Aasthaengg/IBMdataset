N = int(input())
res = 0
for A in map(int, input().split()):
    res += 1/A
print(1/res)