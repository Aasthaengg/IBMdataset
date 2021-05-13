N = int(input())

s = 0
ans = set()
for i in range(1, N+1):
    s += i
    ans.add(i)
    if s >= N:
        break

if N < s:
    ans.remove(s-N)

for a in ans:
    print(a)
