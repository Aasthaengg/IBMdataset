
s = input()
L, R, d = s.split()
L = int(L)
R = int(R)
d = int(d)

# print(L, R, d)

d1 = d
count = 0

while d1 < L:
    d1 += d
    # print(d1)

while d1 <= R:
    count += 1
    d1 += d

print(count)

