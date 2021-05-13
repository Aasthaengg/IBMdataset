n = int(input())
ab = 0
a = 0
b = 0
c = 0
for i in range(n):
    s = input()
    if s[-1] == "A":
        a += 1
    if s[0] == "B":
        b += 1
    if s[-1] == "A" and s[0] == "B":
        c += 1
    for i in range(len(s)-1):
        if s[i] == "A" and s[i+1] == "B":
            ab += 1
ans = ab + min(a,b)
if a == b == c != 0:
    ans = ab + min(a,b) - 1
print(ans)