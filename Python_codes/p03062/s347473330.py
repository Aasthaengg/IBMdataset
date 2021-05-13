N = int(input())
A = list(map(int, input().split()))

minus = 0
x = abs(A[0])
cnt = 0
for a in A:
    minus += (a < 0)
    a = abs(a)
    x = min(x, a)
    cnt += a

if x == 0:
    ans = cnt
elif minus % 2 == 0:
    ans = cnt
else:
    ans = cnt - 2 * x
print(ans)
