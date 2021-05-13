N = int(input())
ans = 100
for A in range(1, N):
    B = N - A
    tmp = sum(list(map(int, str(A)))) + sum(list(map(int, str(B))))
    if ans > tmp:
        ans = tmp
print(ans)