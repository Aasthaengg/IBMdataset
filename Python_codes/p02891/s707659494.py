s = input()
k = int(input())
n = len(s)
res = 0
i = 0
if s.count(s[0]) == n:#全て同じ文字
    print(n*k//2)
    exit()

while i < n-1:
    if s[i] == s[i+1]:
        res += 1
        i += 1
    i += 1

res *= k

if s[0] != s[n-1]: #先頭と末尾の文字が異なる
    print(res)
else:
    a = 0
    b = 0
    i = 0
    while s[i] == s[0]:
        a += 1
        i += 1
    while s[n-1] == s[0]:
        b += 1
        n -= 1
    res -= ((a//2)+(b//2)-((a+b)//2))*(k-1)
    print(res)