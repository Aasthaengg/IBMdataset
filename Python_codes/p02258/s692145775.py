n = input()
n = int(n)

x = input()
x = int(x)

present_min_value = x
max_profit_candidate = 1 - 10**9

for i in range(n - 1):
    a = input()
    a = int(a)
    diff = a - present_min_value
    if diff > max_profit_candidate:
        max_profit_candidate = diff
    if a < present_min_value:
        present_min_value = a

print(max_profit_candidate)