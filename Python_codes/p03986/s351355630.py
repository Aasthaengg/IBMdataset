x = list(input())
x = x[::-1]
counter = 0
ans = len(x)
for i in x:
    if i == "T":
        counter += 1
    elif i == "S" and counter:
        counter -= 1
        ans -= 2
print(ans)