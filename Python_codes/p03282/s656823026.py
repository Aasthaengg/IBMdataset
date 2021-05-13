s = input()
k = int(input())

c1 = 0
num = ""
for c in s:
    if c == "1":
        c1 += 1
    else:
        num = c
        break

if k <= c1:
    print("1")
else:
    print(num)
