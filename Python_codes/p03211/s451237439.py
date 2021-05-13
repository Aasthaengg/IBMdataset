s =input()
m = 100000
for i in range(len(s)-2):
    a=(s[i:i+3])
    m=min(abs(753-int(a)),m)
print(m)