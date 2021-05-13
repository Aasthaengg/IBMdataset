n = int(input().strip())
a = list(map(int, input().split()))
two = 0
four = 0
for e in a:
    if e % 4 == 0:
        four += 1
    elif e % 2 == 0:
        two += 1
if (n - two <= 2 * four) or (two == 0 and n <= (2 * four + 1)):
    print("Yes")
else:
    print("No")
