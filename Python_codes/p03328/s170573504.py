s = input().split()

a = int(s[0])
b = int(s[1])

height = []
p = 1
for i in range(999):
    height.append(p)
    p += 1

c = b - a
sum_num = 0

for i in range(c):
    sum_num += height[i]

answer = sum_num - b

print(answer)

