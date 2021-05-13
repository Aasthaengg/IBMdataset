n = int(input())
a = list(map(int, input().split()))

ans = 99

for i in a:
    j = i
    split_count = 0
    while j % 2 == 0:
        j = j / 2
        split_count += 1
    ans = min(ans, split_count)
print(ans)