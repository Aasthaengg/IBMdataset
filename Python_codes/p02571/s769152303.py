s = list(input())
t = list(input())


max_change = len(t)
for start in range(len(s) - len(t) +1):
    diff =0
    for i in range(len(t)):
        if s[start + i] != t[i]:
            diff += 1
    if diff <= max_change:
        max_change = diff
print(max_change)