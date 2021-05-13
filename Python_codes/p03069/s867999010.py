n = int(input())
s = input()

cnt = 10 ** 9
W = s.count(".")
w = 0
b = 0
for i, j in enumerate(s):
    cnt = min(cnt, b + W - w)
    if j == "#":
        b += 1
    else:
        w += 1
print(min(cnt, b + W - w))