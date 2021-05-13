# C - 100 to 105
ans = 0
X = int(input())
for i in range(1500):
    if 100*i<=X<=105*i:
        ans = 1
        break
print(ans)