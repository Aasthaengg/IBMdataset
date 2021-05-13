k = int(input())
i = 0
s = 0
ans = -1

for z in range(k):
    i += 1
    s = 7 + 10*s
    if s % k != 0:
        s = s % k
    else:
        ans = i
        break

print(ans)