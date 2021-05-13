n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort()
ans = sum(l)

if ans%10 == 0:
    for i in range(n):
        if l[i]%10 != 0:
            ans -= l[i]
            break

    else:
        ans = 0

print(ans)