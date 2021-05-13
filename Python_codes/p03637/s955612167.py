n = int(input())
A = list(map(int, input().split()))

cnt4 = 0
cnt2 = 0
for a in A:
    if a % 4 == 0:
        cnt4 += 1
    elif a % 2 == 0:
        cnt2 += 1

if (n - max(0, cnt2 - 1)) // 2 <= cnt4:
    print("Yes")
else:
    print("No")