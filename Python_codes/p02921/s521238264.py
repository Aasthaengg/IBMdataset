s = list(input())
t = list(input())
c = 0
count = 0
for i in range(3):
    if s[c] == t[c]:
        count += 1
        c += 1
    else:
        c += 1
print(count)