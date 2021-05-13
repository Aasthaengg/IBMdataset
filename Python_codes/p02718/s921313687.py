n, m = map(int, input().split())
a = list(map(int, input().split()))
l = sorted(a, reverse=True)
sum = sum(l) / 4 / m
count = 0

for i in range(len(l)):
    if l[i] >= sum:
        count += 1
    else:
        break


if count >= m:
    print("Yes")
else:
    print("No")
