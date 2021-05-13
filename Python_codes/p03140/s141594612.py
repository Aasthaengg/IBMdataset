a = int(input())
b = (input())
c = (input())
d = (input())
count = 0
for i in range(a):
    if b[i] == c[i] == d[i]:
        count += 0
    elif b[i] == c[i] or b[i] == d[i]  or  c[i] == d[i]:
        count += 1
    else:
        count += 2
print(count)
