s = input()
t = input()
ans = 0

for i, j in zip(s, t):
    ans += i != j

print(ans)
