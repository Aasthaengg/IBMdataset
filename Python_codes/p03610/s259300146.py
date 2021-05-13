s= input()

n = len(s)
res = ""
for i in range(n):
    if i %2 ==0:
        res +=s[i]
print(res)