s = input()
n = len(s)


def point(c0, c1):
    if c0 == "p" and c1 == "p":
        return 0
    if c0 == "p" and c1 == "g":
        return 1
    if c0 == "g" and c1 == "p":
        return -1
    if c0 == "g" and c1 == "g":
        return 0


answer = 0
for i in range(n):
    c0 = "g" if i % 2 == 0 else "p"
    answer += point(c0, s[i])

print(answer)
