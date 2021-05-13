x = int(input())

time1 = x // 11
X = x % 11
time1 *= 2
if X > 6:
    time1 += 2
elif X > 0:
    time1 += 1
print(time1)
