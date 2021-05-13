n = int(input())
ans = 0
a = 0
b = 0
ba = 0
for i in range(n):
    s = input()
    ans += s.count("AB")
    if s[0] == "B":
        if s[-1] == "A":
            ba += 1
        else:
            b += 1
    elif s[-1] == "A":
        a += 1
if a >= 1 or b >= 1:
    print(ans+ba+min(a,b))
else:
    print(ans+max(0,ba-1))