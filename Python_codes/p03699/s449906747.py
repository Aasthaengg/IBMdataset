N = int(input())
s = [int(input()) for i in range(N)]
s.sort()
ans = 0
check = 0
for i in s:
    if i % 10 != 0:
        check = 1
        break

if check == 0:
    ans = 0
else:
    ans = sum(s)
    if ans % 10 == 0:
        for i in s:
            if i % 10 != 0:
                ans -= i
                break

print(ans)
