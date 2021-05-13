N = int(input())
A = list(map(int, input().split()))
tmp = [0] * N
ans = []
ans_m = 0
for i in range(N, 0, -1):
    x = 0
    for j in range(i, N+1, i):
        x += tmp[j-1]
    if x % 2 != A[i-1]:
        tmp[i-1] = 1
        ans_m += 1
        ans.append(str(i))
print(ans_m)
if ans:
    print(" ".join(ans))


