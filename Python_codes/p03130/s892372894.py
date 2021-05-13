A = [0, 0, 0, 0]
for i in range(0, 3):
    a, b = map(int, input().split())
    A[a-1] += 1
    A[b-1] += 1
if max(A) <= 2:
    print("YES")
else:
    print("NO")
