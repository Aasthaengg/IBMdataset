N=int(input())
d=list(map(int, input().split()))
ans=0
while len(d) > 1:
    tmp = d.pop(0)
    for i in d:
        ans += tmp * i
print(ans)