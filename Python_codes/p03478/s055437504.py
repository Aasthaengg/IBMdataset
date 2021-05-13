s = input().split()
n = int(s[0])
a = int(s[1])
b = int(s[2])

sums = []

for i in range(1, n + 1):
    x = i
    check = 0
    while (x > 0):
        y = x % 10
        x = int(x / 10)
        check += y
    if a <= check <= b:
        sums.append(i)

answer = 0
for i in range(len(sums)):
    answer += sums[i]

print(answer)