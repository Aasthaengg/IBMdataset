
l = list(map(int,input().split()))

l.sort()

ans = 0
ans += l[2] - l[1]

if  (l[2] - (ans + l[0])) % 2 == 0:
    ans += (l[2] - (ans + l[0])) / 2
else:
    ans += int((l[2] - (ans + l[0])) / 2) + 2

print(int(ans))
