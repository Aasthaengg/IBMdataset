n = int(input())
a = list(map(int, input().split()))
num = 0
for i in a:
    if i%2 == 1:
        num += 1
if num%2 == 1:
    print('NO')
else:
    print('YES')