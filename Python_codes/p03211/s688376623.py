s = input()

inf = float('inf')
min_ = inf
for i in range(len(s)-2):
    tmp = int(s[i:i+3])
    if abs(753 - tmp) < min_:
        min_ = abs(753 - tmp)
print(min_)