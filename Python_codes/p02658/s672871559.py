N = int(input())

A = list(map(int, input().split()))

flag = 0
ans = 1

if 0 in A:
    print(0)
    flag = 1

for i in range(N):
    if flag == 1:
        break
    ans = ans * A[i]
    if ans > 1000000000000000000 :
        print('-1')
        flag = 1
        break
if flag == 0:
    print(ans)