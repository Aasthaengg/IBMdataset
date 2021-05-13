s = input()
n = len(s)
a = 0

for t in s:
    if t == 'p':
        a += 1


print(n//2 - a)