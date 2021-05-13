n = int(input())
s = [input() for i in range(n)]
a = 0
b = 0
c = 0
cnt = 0
for i in s:
    cnt += i.count("AB")
    if i[0] == "B" and i[-1] == "A":
        a += 1
    elif i[0] == "B":
        b += 1
    elif i[-1] == "A":
        c += 1
if a == 0:
    print(min(b, c) + cnt)
else:
    if b + c == 0:
        print(cnt + a - 1)
    else:
        print(cnt + a + min(b, c))