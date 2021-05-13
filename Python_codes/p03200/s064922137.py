s = input()
n = len(s)

b = 0
b_count = 0
for i in range(n):
    if s[i] == 'B':
        b += i
        b_count += 1

c = 0
for i in range(n-b_count, n):
    c += i

print(c-b)