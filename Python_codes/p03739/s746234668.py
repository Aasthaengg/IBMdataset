
n = int(input())
a = list(map(int, input().split(" ")))



res1 = 0
sum = 0
# sei, hu, sei, hu....
# guu, ki, guu, ki
for i in range(n):
    sum += a[i]
    if sum <= 0 and i%2 == 0:
        res1 += abs(sum) + 1
        sum = 1
    elif sum >= 0 and i%2 == 1:
        res1 += abs(sum) + 1
        sum = -1
    # hutuunitoku


res2 = 0
sum = 0
# hu, sei, hu, sei....
# guu, ki, guu, ki
for i in range(n):
    sum += a[i]
    if sum <= 0 and i%2 == 1:
        res2 += abs(sum) + 1
        sum = 1
    elif sum >= 0 and i%2 == 0:
        res2 += abs(sum) + 1
        sum = -1
    # hutuunitoku

print(min(res1, res2))
