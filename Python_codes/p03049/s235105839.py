n = int(input())
r = 0
a = 0
b = 0
ab = 0
for _i in range(n):
    s = input()
    r += s.count("AB")
    B = 0
    A = 0
    if s[-1]=="A":
        a += 1
    if s[0]=="B":
        b += 1
    if s[-1]=="A" and s[0]=="B":
        ab += 1
if ab == a and ab == b:
    print(r+max(0, ab-1))
else:
    print(r+min(a, b))