n = str(input())
s = 0
e = 0
for i in range(0, len(n)):
    if n[i] == 'A':
        s = i
        break
for i in range(len(n) - 1, 0, -1):
    if n[i] == 'Z':
        e = i
        break
print(int(e - s + 1))
