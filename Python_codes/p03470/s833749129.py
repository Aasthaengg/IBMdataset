n = int(input())
d = []
while n:
    d.append(int(input()))
    n -= 1

d.sort()
before_d = 0
count = 0
for d_temp in d:
    if before_d < d_temp:
        before_d = d_temp
        count += 1

print("{}".format(count))