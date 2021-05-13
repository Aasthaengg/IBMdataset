x, y, z = map(int, input().split())

all = x * y * z

ans1 = int(x/2) * y * z
ans2 = x * int(y/2) * z
ans3 = x * y * int(z/2)

if ans1 == max(ans1, ans2, ans3):
    print(all - ans1 * 2)
elif ans2 == max(ans1, ans2, ans3):
    print(all - ans2 * 2)
else:
    print(all - ans3 * 2)