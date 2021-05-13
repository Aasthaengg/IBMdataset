#不可能な場合の場合分け
n= int(input())
t = [0]+list(map(int, input().split( )))
tmx = max(t)
a = [tmx]+list(map(int, input().split( )))+[0]

if a[0]!= a[1]:
    print(0)
    exit()
ans = 1

for i in range(1,n+1):
    if t[i]>t[i-1]:
        if t[i]>a[i]:
            print(0)
            exit()
        continue
    if a[i]>a[i+1]:
        if a[i]>t[i]:
            print(0)
            exit()
        continue
    if t[i]>t[i-1] and a[i]>a[i+1]:
        if t[i]!=a[i]:
            print(0)
            exit()
        continue

    else:
        ans *= min(t[i],a[i])
        ans %=10**9+7
print(ans)