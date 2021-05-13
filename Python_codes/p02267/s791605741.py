n = int(input())
s = [int(x) for x in input().split()]
q = int(input())
t = [int(x) for x in input().split()]
ans = 0

for x in t:
    c = s.count(x)
    if c != 0:
        ans += 1

print(ans)