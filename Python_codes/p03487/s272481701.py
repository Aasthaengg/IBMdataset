n = int(input())
a = map(int, input().split())

num_count = {}
for num in a:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1
ans = 0
for key in num_count:
    if key < num_count[key]:
        ans += num_count[key] - key
    elif key > num_count[key]:
        ans += num_count[key]
print(ans)
