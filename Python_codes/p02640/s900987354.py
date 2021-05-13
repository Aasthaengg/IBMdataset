x, y = [int(n) for n in input().split(' ')]
crane_cnt = 0
found = False
while crane_cnt <= x:
    turtle_cnt = x - crane_cnt
    if (crane_cnt * 2 + turtle_cnt * 4) == y:
        found = True
        break
    crane_cnt += 1
print('Yes' if found else 'No')
