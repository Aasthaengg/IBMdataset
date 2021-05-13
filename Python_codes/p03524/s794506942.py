s = list(input())

a = b = c = 0
for i in s:
    if i == "a":
        a += 1
    elif i == "b":
        b += 1
    else:
        c += 1

if a*b*c == 0 and a+b+c > 2:
    print("NO")
elif max(a,b,c)-min(a,b,c) >= 2:
    print("NO")
else:
    print("YES")



