s = [input() for _ in range(3)]
d = {"a": 0, "b": 1, "c": 2}
i = [-1] * 3
t = 0
while True:
    i[t] += 1
    if i[t] >= len(s[t]):
        break
    t = d[s[t][i[t]]]
print(["A", "B", "C"][t])