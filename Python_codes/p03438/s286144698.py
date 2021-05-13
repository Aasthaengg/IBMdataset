N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
for i in range(N):
    if a[i] > b[i]:
        cnt2 += a[i] - b[i]
    else:
        cnt1 += (b[i] - a[i] + 1) // 2
        cnt2 += (b[i] - a[i]) % 2

# print(cnt1, cnt2)
if cnt1 >= cnt2:
    print("Yes")
else:
    print("No")