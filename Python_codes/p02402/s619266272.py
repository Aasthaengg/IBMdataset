n = int(input())

s = list(map(int, input().strip().split(' ')))

max = s[0]
min = s[0]
sum = 0
for i in range(n):
    sum = sum + s[i]
    if max < s[i]:
        max = s[i]
    if min > s[i]:
        min = s[i]

print(min, end =" ")
print(max, end =" ")
print(sum)
