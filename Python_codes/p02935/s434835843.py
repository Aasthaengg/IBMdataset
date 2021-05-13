N = int(input())
v = list(map(int,input().split()))
v.sort()
ans = (v[0]+v[1])/2
for x in v[2:]:
    ans = (ans+x)/2
print(ans)