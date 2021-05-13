n,x = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
d = 0
while d<=x and ans<n:
    d += l[ans]
    ans += 1
print(ans if d>x else ans+1)