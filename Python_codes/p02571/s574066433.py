s = input()
t = input()

a = []

for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):
        if t[j] == s[i + j]:
            count += 1
    a.append(count)
print(len(t)-max(a))