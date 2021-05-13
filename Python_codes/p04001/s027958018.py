from itertools import product

s = str(input())
a = list(product(['+', ''], repeat=len(s)-1))


ans = 0
tmp = ""
for i in a:
    tmp = ""
    for j in range(len(s)-1):
        tmp += (s[j]+i[j])
    tmp += s[len(s)-1]
    ans += eval(tmp)
print(ans)
