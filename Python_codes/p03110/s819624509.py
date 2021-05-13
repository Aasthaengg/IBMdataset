n = int(input())
apple = []
for _ in range(n):
    apple.append(list(map(str, input().split())))
count = 0
for i in apple:
    if i[1] == "JPY":
        count += int(i[0])
    else:
        count += 38e4 * float(i[0])
print(count)