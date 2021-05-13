n = int(input())
a = list(map(int, input().split()))
odd = []
even = []
ans = []

for i in range(n):
    if i % 2 == 0:
        odd.append(a[i])
    else:
        even.append(a[i])

if n == 1:
    print(a[0])
    exit()
else:
    if n % 2 == 0:
        even.reverse()
        ans = even + odd
    else:
        odd.reverse()
        ans = odd + even

print(" ".join(map(str,ans)))
