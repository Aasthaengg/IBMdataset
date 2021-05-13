n = int(input())
a = list(map(int, input().split()))

others = 0
rates = [False for i in range(8)]
for i in a:
    if i <= 399: rates[0] = True
    elif i <= 799: rates[1] = True
    elif i <= 1199: rates[2] = True
    elif i <= 1599: rates[3] = True
    elif i <= 1999: rates[4] = True
    elif i <= 2399: rates[5] = True
    elif i <= 2799: rates[6] = True
    elif i <= 3199: rates[7] = True
    else:
        others += 1
        
min_ans = rates.count(True)
if min_ans == 0: min_ans = 1
max_ans = rates.count(True)
if others > 0:
    max_ans += others

print(min_ans, max_ans)