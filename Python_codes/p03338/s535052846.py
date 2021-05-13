n = int(input())
l = list(input())
ans = 0
for i in range(1,n):
    a = set(l[:i])
    b = set(l[i:])
    count = 0
    for j in a:
        if  j in b:
            count += 1
    ans = max(ans,count)
print(ans)