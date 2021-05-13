n = int(input())
for i in range(int(n**0.5)+1):
    if i*i <= n:
        ans = i*i
print(ans)