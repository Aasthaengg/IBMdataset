n = int(input())
s = input()

res = 0

for i in range(1,n):
    temp =""
    x = s[:i]
    y = s[i:]
    for j in range(i):
        if s[j] in y:
            temp +=s[j]
    res = max(res,len(set(temp)))

print(res)