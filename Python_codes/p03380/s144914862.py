N = int(input())
A = list(map(int, input().split()))
A.sort()
m1 = A[-1]
m2 = m1 // 2 + int(m1 % 2 == 1)
ans = [m1, 0]
tmp = 10**9 + 1

for a in A[:len(A) - 1]:
    if tmp > abs(m2 - a):
        tmp = abs(m2 - a)
        ans[1] = a

print(*ans)