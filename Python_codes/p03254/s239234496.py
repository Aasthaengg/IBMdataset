N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

count = 0
for i in a:
    if x < i:
        break
    x -= i
    count += 1
else:
    if x:
        count -= 1

print(count)