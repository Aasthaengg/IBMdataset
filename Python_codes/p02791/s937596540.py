n = int(input())
p = list(map(int,input().split()))
#ans = 0
#for key in range(n):
#    cnt = True
#    for i in range(key+1):
#        if p[i]<p[key]:
#            cnt = False
#    if cnt:
#        ans += 1
#print(ans)

ans = 0
min_left = 2 * 10**5
for i in range(n):
    min_left = min(min_left,p[i])
    if min_left >= p[i]:
        ans += 1
print(ans)