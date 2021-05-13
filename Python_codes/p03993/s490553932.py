n = int(input())
A = list(map(int, input().split()))
checked = [False] * n
ans = 0
for i, a in enumerate(A):
    if checked[i]:
        continue
    if A[a - 1] - 1 == i:
        ans += 1
        checked[i] = True
        checked[a - 1] = True
print(ans)