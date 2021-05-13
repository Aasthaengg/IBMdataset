N = int(input())
S = input()

max_value = 0
value = 0
for c in S:
    if c == 'I':
        value += 1
    elif c == 'D':
        value -= 1
    max_value = max(value, max_value)
print(max_value)    