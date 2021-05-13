n = int(input())
a = list(map(int, input().split()))
ans1 = 0
ans2 = 0
ans3 = 0
for i in range(n):
    if a[i] % 4 == 0:
        ans1 += 1
    elif a[i] % 2 == 0:
        ans2 += 1
    else:
        ans3 += 1
if ans1 + 1 == ans3 and ans2 == 0:
    print("Yes")
elif ans1 >= ans3:
    print("Yes")
else:
    print("No")
