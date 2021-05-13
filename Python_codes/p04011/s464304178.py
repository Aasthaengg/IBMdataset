info = [int(input()) for i in range(4)]

n = info[0]
k = info[1]
x = info[2]
y = info[3]

money = 0

for i in range(n):
    if i >= k:
        money += y
    else:
        money += x

print(money)