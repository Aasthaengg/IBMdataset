n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = [0]*n
ans[n-1] = 1

su = 0
for i in range(n-1):
    su += a[i]
    if su*2 >= a[i+1]:
        ans[i] = 1
        
aa = 0
for i in range(n-1,-1,-1):
    if ans[i] == 1:
        aa += 1
    else:
        break

print(aa)