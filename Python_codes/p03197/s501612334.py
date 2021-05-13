ans = "second"
n = int(input())
for _ in range(n):
    a = int(input())
    if a%2 == 1:
        ans = "first"
        break
print(ans)