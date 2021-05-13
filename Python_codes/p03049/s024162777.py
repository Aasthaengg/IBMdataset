n = int(input())
count = 0
l = [input() for i in range(n)]
a = 0
b = 0
ab = 0
for i in range(n):
    if "AB" in l[i]:
        count += l[i].count("AB")
    if l[i][0] == "B" and l[i][-1] == "A":
        ab += 1
    elif l[i][0] == "B":
        b += 1
    elif l[i][-1] == "A":
        a += 1
if ab >= 2:
    count += ab-1
    ab = 1
x= min(ab,b)
count += x
b -= x
x= min(ab,a)
count += x
a -= x
if a and b:
    count += min(a,b)
print(count)

