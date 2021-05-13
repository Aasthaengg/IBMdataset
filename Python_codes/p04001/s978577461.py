s = input()
n = len(s)-1
ans = 0

for i in range(2**n):
    num = s[0]
    for j in range(n):
        if (i >> j) & 1:
            num += "+"
        num += s[j + 1]
    ans += sum(map(int, num.split("+")))
print(ans)