s = list(input())

phase = "R"

len_s = len(s)

l = [0] * len_s
r = [0] * len_s

#R
c = 0
for i in range(len(s)-1):
    if s[i] == "R":
        c += 1
        if s[i+1] == "L":
            r[i] = (c+1) // 2
            r[i+1] = c // 2
            c = 0

#L
d = 0
for i in reversed(range(1, len(s))):
    if s[i] == "L":
        d += 1
        if s[i-1] == "R":
            l[i] = (d+1) // 2
            l[i-1] = d // 2
            d = 0

a = ["0"] * len_s
for i in range(len_s):
    a[i] = str(l[i] + r[i])

print(" ".join(a))
