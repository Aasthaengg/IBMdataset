n = int(input())
a = list(map(int,input().split()))
count2 = -1
count4 = 0
for i in range(n):
    if a[i] % 4 == 2:
        count2 += 1
    if a[i] % 4 == 0:
        count4 += 1
if count2 >= 1:
    n -= count2
if count4 * 2 + 1 >= n:
    print("Yes")
    exit()
print("No")