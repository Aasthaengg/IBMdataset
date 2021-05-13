n = int(input())

ans = 1
func = [1] * (n + 1)
for i in range(2, n+1):
    for j in range(1, n):
        if i * j > n:
            break
        func[i * j] += 1
    ans += i * func[i]

print(ans)