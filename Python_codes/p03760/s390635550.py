o = list(input())
e = list(input())
result = []
for a, b in zip(o, e):
    result.append(a)
    result.append(b)
if len(o) > len(e):
    result.append(o[-1])
elif len(e) > len(o):
    result.append(e[-1])
print("".join(result))