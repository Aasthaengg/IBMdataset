N = int(input())
n = N - 1
A = list(str(n))
A = list(int(n) for n in A)
ans1 = sum(A) + 1

n = N // 2
A = list(str(n))
A = list(int(n) for n in A)
ans2 = 2 * sum(A)

if N % 2 == 0:
    ans = min(ans1, ans2)
else:
    ans = min(ans1, ans2 + 1)

print(ans)