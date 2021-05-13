n = input()
sum = 0
ans = 0

if len(n) == 1:
    ans = n
elif len(n) == 2:
    ans = 9
elif len(n) == 3:
    n = int(n)
    ans = ((n-100)+1)+9
elif len(n) == 4:
    ans = 9+900
elif len(n) == 5:
    n = int(n)
    ans = ((n-10000)+1)+900+9
else:
    ans = 90000+900+9

print(ans)