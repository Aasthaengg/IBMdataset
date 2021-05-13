N, A, B = map(int,input().split())

ans = 0
for i in range(N+1):
    moji = str(i)
    n = 0
    for j in range(len(moji)):
      n += int(moji[j])

    if A <= n and n <= B:
        ans += i

print(ans)