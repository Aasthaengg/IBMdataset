n = int(input())
ans = 0
for i in range(1, n+1):
    if int(i * 1.08) == n:
        ans = i

if ans == 0:
    print(":(")
else:
    print(ans)