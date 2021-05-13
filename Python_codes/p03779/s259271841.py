X = int(input())
now = 0
time = 0
for i in range(1,10**5):
    now += i
    time += 1
    if now >= X:
        break
print(time)