N = int(input())
a = list(map(int,input().split()))

ans = 0
right = 0
s = 0
for left in range(N):
    while right < N and ((s^a[right] == s + a[right])):
        s += a[right]
        right += 1


    ans += (right - left)

    if left == right:
        right += 1
    else:
        s -= a[left]
print(ans)
