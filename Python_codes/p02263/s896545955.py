rows = input().split()


ans = []
for i in rows:
    if i == "+":
        a = ans.pop()
        b = ans.pop()
        ans.append(a + b)
    elif i == "-":
        a = ans.pop()
        b = ans.pop()
        ans.append(b - a)
    elif i == "*":
        a = ans.pop()
        b = ans.pop()
        ans.append(a * b)
    else:
        ans.append(int(i))

print(' '.join(map(str, ans)))