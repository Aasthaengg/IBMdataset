INF = 1000000007
s = list(input())
t = list(input())
lis = [[0] for i in range(26)]
for i in range(len(s)):
    lis[ord(s[i])-ord('a')].append(i+1)

for i in range(26):
    lis[i].append(INF)
#print(lis)

def binary_search(val,lis):
    ng = 0
    ok = len(lis)-1
    while abs(ng-ok) > 1:
        mid = (ok+ng)//2
        if lis[mid] > val:
            ok = mid
        else:
            ng = mid
        #print(ok,ng)
    return lis[ok]
# print(binary_search(5,[3,4,5,6,7,8]))

ans = 0
p = 0
for i in t:
    j = ord(i) - ord('a')
    if len(lis[j]) == 2:
        print(-1)
        exit()
    val = binary_search(p,lis[j])
    p = val
    if val == INF:
        ans += len(s)
        p = binary_search(0,lis[j])
    #print(p)
print(ans + p)
