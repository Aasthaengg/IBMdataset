n = int(input())
s = input()
t = input()

u = n
for i in range(n):
    if s[i:] == t[:(n-i)]:
        u = i
        break

print(u+n)