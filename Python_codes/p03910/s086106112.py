N = int(input())
s = 0
ans = set()
for i in range(1,N+1):
    ans.add(i)
    s += i
    if s >= N: break
if s-N in ans:
    ans.remove(s-N)

print(*ans, sep='\n')