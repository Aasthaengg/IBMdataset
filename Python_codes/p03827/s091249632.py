n = int(input())
s = input()
l = list(s)

count = [0]
c = 0
for i in l:
    if i == 'I':
        c += 1
        count.append(c)
    elif i == 'D':
        c -= 1
        count.append(c)
print(max(count))