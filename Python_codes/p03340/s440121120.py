N = int(input())
a = list(map(int,input().split()))
l,r = 0,1
ans = 0

# a中の区間[l,r)について見ていく
nowx = 0
nows = 0
while True:
    if l == N:
        break
    if r == N+1:
        break
    if nowx^a[r-1] == nows+a[r-1]: # いま条件を満たしていればansに変更を加えてしきりを右側に移す
        nowx ^= a[r-1]
        nows += a[r-1]
        ans += r-l
        r += 1
        #l += 1 ### 2の場合
    elif r == l:
        r += 1
        l += 1
    else:
        nowx ^= a[l]
        nows -= a[l]
        l += 1
        #r += 1 ### 2の場合
print(ans)
