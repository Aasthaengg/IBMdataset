n = int(input().replace(' ', ''))

ans = 'No'
for i in range(1000):
    if n == i ** 2:
        ans = 'Yes'
print(ans)
