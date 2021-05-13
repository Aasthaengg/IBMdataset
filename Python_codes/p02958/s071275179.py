n = int(input())
li1 = list(map(int,input().split()))
li2 = sorted(li1)

cnt = 0

for i in range(n):
    if li1[i] != li2[i]:
        cnt += 1

if cnt>2:
    print('NO')
else:
    print('YES')
