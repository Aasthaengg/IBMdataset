n = int(input())
alist=list(map(int,input().split()))

alist = sorted(alist,reverse=True)
ans = alist[0]
count = 1
flag = True
for i in range(n-2):
    if flag:
        ans += alist[count]
        flag = False
    else:
        ans += alist[count]
        count += 1
        flag = True

print(ans)