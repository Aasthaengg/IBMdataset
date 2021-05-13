X, Y = map(int, input().split())

sum = 0
if X == 1:
    sum += 300000
elif X == 2:
    sum += 200000
elif X == 3:
    sum += 100000

if Y == 1:
    sum += 300000
elif Y == 2:
    sum += 200000
elif Y == 3:
    sum += 100000

if sum == 600000:
    sum += 400000

print(sum)
