N = int(input())
s = []
for _ in range(N):
    si = int(input())
    s.append(si)

s.sort()
# print(s)

not_10 = []

for si in s:
    if si % 10 != 0:
        not_10.append(si)

ans = sum(s)

while ans % 10 == 0:
    if len(not_10) > 0:
        ans -= not_10.pop(0)
    else:
        print(0)
        exit()

print(ans)
