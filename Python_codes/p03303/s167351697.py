s = list(input())
w = int(input())
t = []
for i in range(0, len(s), w):
    t.append(s[i])
print("".join(t))