n = int(input())
a = [int(s) for s in input().split()]

count = 0
same_color = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        same_color += 1
    else:
        count += same_color // 2
        same_color = 1
if same_color > 1:
    count += same_color // 2
print(count)