N = int(input())
A_list = list(map(int, input().split()))
ans = 1
if 0 in A_list:
    ans = 0
else:
    for A in A_list:
        ans *= A
        if ans > 10**18:
            ans=-1
            break

print(ans)
