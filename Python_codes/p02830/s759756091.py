n = int(input())
moji = input().split()

s = moji[0]
t = moji[1]

a = '1'

for i in range(n):
    a += s[i]
    a += t[i]
print(a[1:])
