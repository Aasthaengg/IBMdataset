s = input()
k = int(input())

f = 1
d = 0

for c in s:
    if int(c) != 1:
        f = int(c)
        break
    else:
        d += 1

if d >= k:
    print(1)
else:
    print(f)