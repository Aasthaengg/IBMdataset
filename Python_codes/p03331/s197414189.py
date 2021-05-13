n = input()
ans = 0
for i in range(len(n)):
    ans += int(n[i])
if ans == 1:
    ans = 10
print(ans)