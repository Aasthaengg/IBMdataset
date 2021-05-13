s = input()
t = input()
min_count = len(s)
for i in range(len(s) - len(t)+1):
    count = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            count += 1
    if min_count > count:
        min_count = count
print(min_count)
