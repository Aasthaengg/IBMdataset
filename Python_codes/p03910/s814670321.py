n = int(input())
ans = set([0])
for i in range(1, n+1):
    ans.add(i)
    n -= i
    if n<=0:
        break

ans = list(ans)
ans.remove(0)
if n!=0:
    ans.remove(-n)

for a in ans:
    print(a)