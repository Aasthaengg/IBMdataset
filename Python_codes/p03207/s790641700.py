n = int(input())
p = []
for i in range(n):
    p.append(int(input()))
ans = sum(p)
ans -= max(p)//2
print(ans)
