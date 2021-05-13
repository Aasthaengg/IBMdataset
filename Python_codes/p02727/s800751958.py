X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

ans = sorted(P[:X] + Q[:Y])

for i in range(min(C, X+Y)):
    if R[i] > ans[i]:
        ans[i] = R[i]

print(sum(ans))