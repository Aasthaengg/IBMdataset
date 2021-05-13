items = ['A', 'C', 'G', 'T']

s = input()
n = len(s)
t = [0] * (n+1)

for i in range(n):
    if s[i] in items:
        t[i + 1] += t[i] + 1
    else:
        t[i + 1] += 0
print(max(t))

