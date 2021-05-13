n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
a_max = a_list[-1]

divisible = [False] * (a_max + 1)

count = 0
i = 0
for i in range(n):
    if divisible[a_list[i]]:
        continue
    if i < n - 1 and a_list[i] == a_list[i + 1]:
        while i < n - 1 and a_list[i] == a_list[i + 1]:
            i += 1
    else:
        count += 1
    x = a_list[i]
    while x <= a_max:
        divisible[x] = True
        x += a_list[i]
print(count)