N = int(input())
A = list(map(int,input().split()))
ans = 1
if 0 in A:
    print(0)
else:
    for i in A:
        ans = ans * i
        if ans > 10**18:
            ans = -1
            break
    print(ans)