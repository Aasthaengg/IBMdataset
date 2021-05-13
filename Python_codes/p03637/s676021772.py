n = int(input())
a = list(map(int, input().split()))

odd_cnt = 0
multi_4 = 0
for i in range(n):
    if a[i] % 4 == 0:
        multi_4 += 1
    elif a[i] % 2 == 1:
        odd_cnt += 1

if multi_4 + odd_cnt == n:
    print("Yes" if multi_4 >= odd_cnt - 1 else "No")
else:
    print("Yes" if multi_4 >= odd_cnt else "No")