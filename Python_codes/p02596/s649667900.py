K = int(input())

val = 7 % K

ans = -1
for i in range(1, 10**6):
    if val == 0:
        ans = i
        break
    val = (val * 10 + 7) % K

print(ans)