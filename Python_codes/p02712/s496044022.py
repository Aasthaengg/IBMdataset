N = int(input())
fizz = N // 3
buzz = N // 5
fzbz = N // 15
ans = (N+1)*N // 2
ans -= buzz * (5 * buzz + 5) // 2
ans -= fizz * (3 * fizz + 3) // 2
ans += fzbz * (15 * fzbz + 15) // 2
print(ans)
