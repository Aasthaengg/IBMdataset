k = int(input())
s = input()
ans = s
if len(s) > k:
    ans = "%s..." % s[:k]

print(ans)
