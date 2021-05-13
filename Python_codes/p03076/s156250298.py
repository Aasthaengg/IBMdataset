t = []
for i in range(5):
    t.append(int(input()))

s = []
for i in range(5):
    s.append(t[i] % 10)

o = 5
p = 10
for i in range(5):
    if s[i] > 0:
        if p > s[i]:
            o = i
            p = s[i]

m = 0
for i in range(5):
    if i != o:
        if s[i] == 0:
            m += t[i]
        else:
            m += t[i] - t[i] % 10 + 10

if o != 5:
    m += t[o]
print(m)