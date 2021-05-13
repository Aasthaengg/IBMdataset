x = int(input()) - 1

time1 = x // 11
X = x % 11
time1 *= 2
if X > 5:
    time1 += 2
else:
    time1 += 1
print(time1)
