n = int(input())
A = list(map(int, input().split()))

t = 0
for i in range(n):
    if A[i] % 2 == 1:
        t += 1
if t%2 == 1:
    print("NO")
else:
    print("YES")