T = [s for s in input().strip()]

total_sum = 0
pre = T[0]
if pre == "D":
    total_sum = 1
elif pre == "?":
    total_sum = 1
    T[0] = "D"
    pre = "D"

for i in range(1, len(T)):
    now = T[i]
    if now == "D" and pre == "P":
        total_sum += 2
        pre = "D"
    elif now == "D" and pre == "D":
        total_sum += 1
        pre = "D"
    elif now == "?" and pre == "D":
        total_sum += 1
        pre = "D"
        T[i] = "D"
    elif now == "?" and pre == "P":
        total_sum += 2
        pre = "D"
        T[i] = "D"
    else:
        pre = now

print("".join(T))