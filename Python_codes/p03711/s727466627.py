x, y = map(int, input().split())
val1 = [1, 3, 5, 7, 8, 10, 12]
val2 = [4, 6, 9, 11]
val3 = [2]

cnt1 = 0
for i in range(len(val1)):
    if val1[i] == x or val1[i] == y:
        cnt1 += 1

cnt2 = 0
for i in range(len(val2)):
    if val2[i] == x or val2[i] == y:
        cnt2 += 1

if cnt1 == 2 or cnt2 == 2:
    print('Yes')

else:
    print('No')