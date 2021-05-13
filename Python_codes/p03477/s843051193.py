A, B, C, D = list(map(int, input().split()))
l = A+B
r = C+D
if l > r:
    ans = "Left"
elif l < r:
    ans = "Right"
else:
    ans = "Balanced"
print(ans)
