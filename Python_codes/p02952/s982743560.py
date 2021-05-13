n = input()

l = [9, 909, 90909]
ans = 0
if len(n) == 1:
    ans = int(n)
elif len(n) != 1 and len(n) % 2 == 1:
    ans = int(n) - 10 ** (len(n) - 1) + 1 + l[len(n) // 2 - 1]
else:
    ans =  l[len(n) // 2 - 1]

print(ans)
