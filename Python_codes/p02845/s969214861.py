N = int(input())
A = list(map(int,input().split()))
x,y,z = 0,0,0
ans = 1
mod = 10**9+7
for i in range(N):
    c = [x,y,z].count(A[i])
    if c == 0:
        print(0)
        exit(0)
    ans = ans*c % mod
    if x == A[i]:
        x += 1
    elif y == A[i]:
        y += 1
    else:
        z += 1
    l = list(sorted([x,y,z]))
    x,y,z = l[0],l[1],l[2]

print(ans)