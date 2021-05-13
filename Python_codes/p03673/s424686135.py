n = int(input())
a = list(map(int, input().split()))

left = []
right = []

for i in range(n):
    if i % 2 == 0:
        left.append(a[i])
    else:
        right.append(a[i])
if n % 2 == 0:
    right.reverse()
    arr = right + left
    ans = " ".join(map(str, arr))
    print(ans)
else:
    left.reverse()
    arr = left + right
    ans = " ".join(map(str, arr))
    print(ans)