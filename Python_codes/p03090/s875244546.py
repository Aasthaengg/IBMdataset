n = int(input())
l = []
if n%2==1:
    for i in range((n-1)//2):
        l.append([i+1,n-1-i])
    l.append([n,n])
else:
    for i in range(n//2):
        l.append([i+1,n-i])
ans = []
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            continue
        ret1 = [l[i][0],l[j][0]]
        ret2 = [l[i][0],l[j][1]]
        ret3 = [l[i][1],l[j][0]]
        ret4 = [l[i][1],l[j][1]]
        ret1.sort()
        ret2.sort()
        ret3.sort()
        ret4.sort()
        ret = [ret1,ret2,ret3,ret4]
        for ret_ in ret:
            if not ret_ in ans:
                ans.append(ret_)
print(len(ans))
for ans_ in ans:
    print(ans_[0],ans_[1])