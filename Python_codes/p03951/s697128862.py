n = int(input())
s = input()
t = input()
if s == t:
    print(n)
    exit()
t = t[::-1]
s = s[::-1]
res = n
j = 0
for i in range(n):
    if s[j]==t[i]:
        j += 1
    else:
        res += 1
print(res)