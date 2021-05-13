n = int(input())
Arr = [0] * (n + 1)
for num in range(1, n+1):
    for i in range(1, n // num + 1):
        Arr[i * num] += 1
ans = 0
for i in range(1, n+1):
    ans += Arr[i] * i
print(ans)
