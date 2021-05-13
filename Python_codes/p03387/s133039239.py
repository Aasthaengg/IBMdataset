ABC= list(map(int, input().split()))
M = max(ABC)
ans = 0
for i in range(3):
    ABC[i] = M - ABC[i]
    ans += ABC[i] // 2
    ABC[i] = ABC[i] % 2

if sum(ABC) == 2:
    ans += 1
elif sum(ABC) == 1:
    ans += 2
else:
    ans += 0
print(ans)
