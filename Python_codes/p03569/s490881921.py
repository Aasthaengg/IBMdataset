from sys import stdin

s = stdin.readline().rstrip()
k = ""
for i in range(len(s)):
    if s[i] != "x":
        k += s[i]

if k != k[::-1]:
    print(-1)
    exit()

man = (len(k)+1)//2
point = 0
for i,j in enumerate(s):
    if j != "x":
        point += 1
    if point == man:
        kotae = i
        break

a = s[:kotae+1]
b = s[kotae:][::-1]

A = len(a)
B = len(b)

point_a = 0
point_b = 0

total = 0

while point_a < A and point_b < B:
    if a[point_a] == b[point_b]:
        point_a += 1
        point_b += 1
    elif a[point_a] == "x" and b[point_b] != "x":
        point_a += 1
        total += 1
    else:
        point_b += 1
        total += 1

print(total)