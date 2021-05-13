# 136 B

s = int(input())
sum = 0

for i in range(1, s+1):
    if (len(str(i)) % 2 != 0):
        sum += 1

print(sum)