n = int(input())
A = [int(input()) for _ in range(n)]

for a in A:
    if a != 1:
        break
else:
    print('first')
    exit()

cnt = 0
for a in A:
    if a%2 == 0:
        cnt += 1
if cnt == n:
    print('second')
else:
    print('first')
