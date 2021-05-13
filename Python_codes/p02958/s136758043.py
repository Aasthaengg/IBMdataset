n = int(input())
pl = list(map(int,input().split()))

temp = 0

for i in range(n):
    if pl[i] != i+1:
        temp += 1

if temp <= 2 :
    print('YES')
else:
    print('NO')
