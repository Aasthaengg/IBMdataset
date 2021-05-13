s = list(input())
result = []
for i in set(s):
    x = [0]
    y = 0
    for j in range(len(s)):
        if s[j] == i:
            x.append(y)
            y = 0
        else:
            y += 1
    x.append(y)
    if s[-1] == i:
        result.append(max(x))
    else:
        result.append(x[-1]+max(0, max(x[:-1])-x[-1]))
print(min(result))