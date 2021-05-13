n = int(input())
A = list(map(int,input().split()))
A.sort()
ls = []
pre = A[0]
cnt = 1
for i in range(n):
    if A[i] == pre:
        cnt+=1
    else:
        ls.append((pre,cnt))
        cnt = 1
    pre = A[i]
ls.append((pre,cnt))
ans = 0
pre = 0
for num,cnt in ls:
    if cnt>=2:
        if cnt>=4:
            ans = num**2
        else:
            ans = num*pre
        pre = num
print(ans)
