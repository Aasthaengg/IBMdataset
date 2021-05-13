n = int(input())

s = str(n)
l = len(s)
sum1 = 0

s = str(n)
for i in range(l):
    sum1 +=int(s[i])

ans = 0
for i in range(l):
    if i == 0:
        sum2 = (int(s[i])-1) + 9*(l-1) 
    else:
        sum2 = int(s[0]) + 9*(l-2) + int(s[i])-1

    ans = max(ans,max(sum1,sum2))

print(ans)