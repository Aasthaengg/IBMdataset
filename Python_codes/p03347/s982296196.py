N = int(input())

ans = -1
tmp = -1 #直前の数字
for i in range(N):
    A = int(input())
    if A > i:
        print (-1)
        exit()
    if tmp + 1 < A:
        print (-1)
        exit()
    if tmp + 1 == A:
        ans += 1
        tmp += 1
    else:
        ans += A
        tmp = A

print (ans)