N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0
total = sum(A)
thre = total / (4 * M)

for a in A:
    if a < thre:
        break
    ans += 1

if ans >= M:
    print("Yes")
else:
    print("No")
