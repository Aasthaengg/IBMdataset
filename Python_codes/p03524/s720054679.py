from collections import Counter

s = input()

d = {
    "a": 0,
    "b": 0,
    "c": 0
}

for x in s:
    d[x] += 1

result = list(d.values())

print("YES" if max(result) - min(result) <= 1 else "NO")