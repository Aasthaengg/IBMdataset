k, x = map(int, input().split())
ans = ''
for i in range(2 * k - 1):
    ans += str(x - (k - 1) +  i) + ' '
print(ans)