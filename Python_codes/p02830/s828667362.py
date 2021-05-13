n =int(input())
s,t = input().split()
m = "a"
for i in range(n):
    m = m+s[i]+t[i]

print(m[1::])
