n = int(input())
a = list(map(int,input().split()))

tmp = True
ans = 0
for i in range(n):
    if i+1 == a[i]:
        if tmp == False:
            tmp = True
        else:
            ans += 1
            tmp = False
    else:
        tmp = True

print(ans)

