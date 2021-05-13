n = int(input())
A = tuple(map(int, input().split()))
cnt = 0
zero = False
for a in A:
    if a < 0:
        cnt += 1
    elif a == 0:
        zero = True

if cnt%2 == 0 or zero:
    print(sum(map(abs, A)))
else:
    A = sorted(map(abs, A))
    print(sum(A) - 2*A[0])
