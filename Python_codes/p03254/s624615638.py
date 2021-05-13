# https://atcoder.jp/contests/agc027/tasks/agc027_a
n, x = [int(i) for i in input().split()]
A = sorted([int(i) for i in input().split()])

if sum(A) == x:
    ans = n
elif sum(A) < x:
    ans = n - 1
else:
    ans = 0
    for i in range(n):
        if A[i] <= x:
            if i == n - 1:
                if x == A[i]:
                    ans += 1
            else:
                x -= A[i]
                ans += 1
        else:
            continue

print(ans)
