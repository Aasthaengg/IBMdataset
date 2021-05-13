x = int(input())

total = 0
now = 1

while total < x:
    total += now
    now += 1

print(now-1)
