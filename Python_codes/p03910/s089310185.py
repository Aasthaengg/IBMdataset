N = int(input())
s = set()

ans = 0
for i in range(1, N + 1):
    ans += i
    s.add(i)
    if ans >= N:
        break

if ans > N:
    s.remove(ans - N)

for n in s:
    print(n)