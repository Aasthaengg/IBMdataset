n = int(input())
ans = []
Sum = 0
for i in range(1, 10**4):
    Sum += i
    ans.append(i)
    if Sum >= n:
        break

if Sum == n:
    print(*ans)
else:
    ans.remove(Sum - n)
    print(*ans)