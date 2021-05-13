n = int(input())
result = 0
for i in range(n):
    l, r = list(map(int, input().split()))
    if l == r:
        result += 1
    else:
        result += r - l + 1
print(result)