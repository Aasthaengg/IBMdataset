n = int(input())
ans = 10**5+1
for a in range(1, n//2+1):
    a,b = list(str(a)), list(str(n-a))
    ans = min(ans, sum(list(map(int, a)))+sum(list(map(int,b))))
print(ans)