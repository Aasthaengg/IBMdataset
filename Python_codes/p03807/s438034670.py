N = int(input())
A = list(map(int, input().split()))

odd, even = 0, 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

d, m = divmod(odd, 2)
even += d
odd = m

if odd == 0:
    ans = "YES"
else:
    ans = "YES" if even == 0 else "NO"

print(ans)
