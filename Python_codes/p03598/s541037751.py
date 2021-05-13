n = int(input())
k = int(input())
x = list(map(int, input().split()))

res = 0

for i in x:
    if k - i < i:
        res += 2 * (k - i)
    else:
        res += 2 * i
print(res)
