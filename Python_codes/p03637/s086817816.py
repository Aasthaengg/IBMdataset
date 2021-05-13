n = int(input())
ns = map(int, input().split())
four = [0, 0, 0, 0]
for i in ns:
    four[i%4] += 1
if four[2] == 0 and n - 1 - 2*four[0] <= 0:
    print('Yes')
elif n - four[2] - 2*four[0] <= 0:
    print('Yes')
else:
    print('No')