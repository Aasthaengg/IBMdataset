n,m = map(int, input().split())
ac = [0]*n
wa = [0]*n
ans = 0

for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == 'AC' and ac[p] == 0:
        ac[p] = 1
        ans += wa[p]
    wa[p] += 1
print(sum(ac), ans)
