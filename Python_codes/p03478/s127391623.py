a, b, c = map(int, input().split())
start_number = 0
sum_number = 0
for d in range(0, a+1, 1):
    for e in str(d):
        sum_number += int(e)
    if b <= sum_number <= c:
        start_number += d
        sum_number = 0
    else:
        sum_number = 0
print(start_number)