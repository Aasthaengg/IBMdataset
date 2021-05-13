H = int(input())

i = 1
ans = 1
while H > 1:
    H //= 2
    ans += 2 ** i
    i += 1
print(ans)