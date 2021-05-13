N = int(input())
A = [int(input()) for _ in range(N)]

if A[0] != 0:
    print(-1)
    exit()

ans = 0
tmp = 0
for num in reversed(A):
    if tmp > 0:
        if num == tmp-1:
            tmp = num
        elif num >= tmp:
            ans += num
            tmp = num
        elif num < tmp-1:
            print(-1)
            exit()

    else:
        ans += num
        tmp = num
        

print(ans)