s = list(input())
n = len(s) - 1 
p = 0
for i in range(2**n):
    m = int(s[0])
    x = i
    for j in range(n):
        if x % 2 != 0:
            p += m
            m = int(s[j+1])
        else:
            m = m * 10 + int(s[j+1])
        x = x // 2
    p += m
print(p)     