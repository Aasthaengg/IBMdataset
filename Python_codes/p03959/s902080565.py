MOD = 10**9 + 7
n = int(input())
t = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]

height = [0] * n
height[0] = t[0]
for i in range(1, n):
    if t[i] > t[i-1]:
        height[i] = t[i]
        if t[i] > a[i]:
            print(0)
            exit()
if height[-1] == 0:
    height[-1] = a[-1]
elif height[-1] != a[-1]:
        print(0)
        exit()

for i in range(n-1, 0, -1):
    if a[i] < a[i-1]:
        if height[i-1] == 0:
            height[i-1] = a[i-1]
            if a[i-1] > t[i-1]:
                print(0)
                exit()
        elif height[i-1] != a[i-1]:
            print(0)
            exit()

ans = 1
for i, item in enumerate(height):
    if item == 0:
        ans *= min(t[i], a[i])
        ans %= MOD

print(ans)