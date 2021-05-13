n = int(input())
s = input()
t = input()

ans = n

for i in range(n):
    if s[i:] == t[:-i + n]:
        break
    else:
        ans += 1

print(ans)
