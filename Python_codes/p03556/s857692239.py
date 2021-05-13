n = int(input())
ans = 0
for i in range(1, int(n**0.5)+1):
    if i*i <= n:
        ans = i*i
print(ans)
