N = int(input())
a = list(map(int, input().split()))
cnt_4 = 0
cnt_2 = 0
for i in range(N):
    if a[i]%4 == 0:
        cnt_4 += 1
    elif a[i]%2 == 0:
        cnt_2 += 1
if cnt_4 + cnt_2//2 >= N//2:
    print("Yes")
else:
    print("No")