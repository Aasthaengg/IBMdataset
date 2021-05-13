n = int(input())
l = len(str(n))

if l == 1:
    print(n)
    exit()
ans = 9
if l % 2 == 1:
    ans += n + 1 - 10 ** (l - 1)

for i in range(3,l):
    if i % 2 == 1:
       ans += 10 ** i - 10 ** (i - 1)
print(ans)
