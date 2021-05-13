A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [list(map(int,input().split())) for _ in range(M)]

amin = min(a)
bmin = min(b)
ans = amin + bmin
for c_ in c:
    tmp = a[c_[0]-1] + b[c_[1]-1] - c_[2]
    ans = min(ans,tmp)

print(ans)