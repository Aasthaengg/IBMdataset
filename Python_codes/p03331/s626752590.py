n = int(input())
ans = float("inf")
for i in range(1,n):
    ans = min(ans,sum(map(int,str(i)))+sum(map(int,str(n-i))))
print(ans)