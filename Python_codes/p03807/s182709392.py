n = int(input())
a = list(map(int, input().split()))

odd_count = 0
for i in a:
    if i % 2:
        odd_count += 1
print('NO' if odd_count % 2 else 'YES')
