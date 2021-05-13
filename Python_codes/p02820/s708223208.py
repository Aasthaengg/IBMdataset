n,k = map(int, input().split())
r,s,p = map(int, input().split())
t = str(input())
num = p*t.count('r') + r*t.count('s') + s*t.count('p')
w = ""
for i in range(n):
    if t[i] == "r":
        x = "p"
        y = p
    elif t[i] == "s":
        x = "r"
        y = r
    else:
        x = "s"
        y = s
    if i < k:
        w += x
    else:
        if w[i-k] == x:
            num -= y
            w += "q"
        else:
            w += x
print(num)