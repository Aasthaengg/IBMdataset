s = list(map(str,input()))
a,b,c = 0,0,0

for i in range(len(s)):
    if s[i] == "a":
        a += 1
    elif s[i] == "b":
        b += 1
    else:
        c += 1

if abs(a-b) <= 1 and abs(b-c) <= 1 and abs(c-a) <= 1:
    print("YES")
else:
    print("NO")