h,w,k = [int(x) for x in input().split()]
i = 0
ans = [[1]*w for _ in range(h)]
flag = 0
for j in range(h):
    i+=1
    x = list(input())
    cnt = 0
    for z in range(len(x)):
        if x[z]=="#":
            cnt+=1
            if cnt>=2:
                i+=1
        ans[j][z] = i
        if flag:
            for kk in range(j):
                ans[kk][z] = i
    
    if cnt>=1 and flag:
        flag = 0
    if (cnt==0 and j==0) or flag:
        flag = 1
        i-=1
    if cnt==0 and j>=1 and not flag:
        for z in range(len(x)):
            ans[j][z] = ans[j-1][z]
        i-=1
for j in ans:
    print(" ".join([str(x) for x in j]))

