N = int(input())
a = input().split()

flg = False
old = a[0]

cnt = 0
for i in range(1,N):
    if a[i] == old and not flg:
        cnt += 1
        flg = True
    else:
        flg = False
    old = a[i]

print(int(cnt))