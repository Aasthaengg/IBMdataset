n = int(input())
a = [int(input()) for i in range(n)]

res = 1
i = 1
for k in range(n):
    if a[i-1]==2:
        break
    else:
        i = a[i-1]
        res += 1
else:
    res = -1
    
print(res)
