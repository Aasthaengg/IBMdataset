n = int(input())
k = int(input())
x = list(map(int, input().split()))

result = 0
for x_ in x:
    result += min(x_, (k - x_))

print(2 * result)