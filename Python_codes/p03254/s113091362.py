N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
sum = 0
ans = 0
for i,a in enumerate(A):
    sum += a

    if sum == x:
        ans = i + 1
        break
    elif sum > x:
        break
    elif i + 1 == N and sum < x:
        ans = i
        break
    ans = i + 1


print(ans)
