abc = list(map(int, input().split()))
abc.sort()
a, b, c = abc[0], abc[1], abc[2]
if a % 2 == b % 2:
    ans = (2 * c - a - b) // 2
else:
    ans = (2 * c + 1 - a - b) // 2 + 1
print(ans)
