n,l = map(int,input().split())
ans = list(i+l for i in range(n))
m = 10**10
for i in ans:
    if abs(m)>abs(i):
        m = i
print(sum(ans)-m)