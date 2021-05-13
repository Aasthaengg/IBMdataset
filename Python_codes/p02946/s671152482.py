k,x = map(int,input().split())
ans = set([x])
for i in range(1,k):
    ans.add(x-i)
    ans.add(x+i)

print(*sorted(list(ans)))