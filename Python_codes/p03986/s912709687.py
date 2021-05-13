x = input()
ls = []
ans = len(x)
for i in range(len(x)):
    if x[i] == "S":
        ls.append("S")
    else:
        if len(ls):
            ls.pop()
            ans -= 2
print(ans)
