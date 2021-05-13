
a, b = list(map(int, input().split(' ')))
ans = b * pow(b-1, a-1)
print(ans)

