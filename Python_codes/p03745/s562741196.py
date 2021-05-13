N = int(input())
A = list(map(int, input().split()))

prev = A[0]
ans = 1
for i in range(1, N):
    if A[i] > prev:
        pls = "plus"
        break
    elif A[i] < prev:
        pls = "minus"
        break
else:
    print(1)
    exit()

for i in range(1, N):
    if pls == "plus" and prev > A[i]:
        prev = A[i]
        ans += 1
        pls = "even"
        continue
    if pls == "minus" and prev < A[i]:
        prev = A[i]
        ans += 1
        pls = "even"
        continue
    if pls == "even" and prev < A[i]:
        pls = "plus"
    elif pls == "even" and prev > A[i]:
        pls = "minus"
    prev = A[i]
print(ans)