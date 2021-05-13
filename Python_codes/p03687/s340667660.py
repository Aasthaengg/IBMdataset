s = input()
lon = len(s)
lis = list(s)
ans = 10000
#print(lis)
for i in s:
    cnt=0
    lef = []

    ind = [j for j, x in enumerate(lis) if x==i]
    pre=0
    for ma in ind:
        lef.append(ma-pre)
        pre = ma+1
    lef.append(lon-ma-1)
    ans_ten = max(lef)
    ans = min(ans,ans_ten)

print(ans)