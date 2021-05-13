s = list(input())
l = ["#"] * (len(s)-1)
ans = 0
for i in range(2**(len(s)-1)):
    for j in range(len(s)-1):
        if (i>>j)&1:
            l[j] = "+"
    x = []
    for j in range(len(s)*2-1):
        if j % 2 == 0:
            x.append(s[j//2])
        else:
            if l[(j-1)//2] == "+":
                x.append("+")
    ans += sum(list(map(int, "".join(x).split("+"))))
    l = ["#"] * (len(s)-1)
print(ans)