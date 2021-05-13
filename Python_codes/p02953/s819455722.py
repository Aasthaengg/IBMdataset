n = int(input())
h = list(map(int, input().split()))
can_build = True
for i in range(n-1, 0, -1):
    diff = h[i-1] - h[i]
    if diff == 1:
        h[i - 1] -= 1
    elif diff > 1:
        can_build = False
        break
print("Yes" if can_build else "No")