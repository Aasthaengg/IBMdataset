(a, b) = map(int, input().split())

for i in range(1, 13):
    if (i > a) or ((i == a) and (i > b)):
        break
    ans = i
print(ans)
